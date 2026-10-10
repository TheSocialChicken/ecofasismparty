#!/usr/bin/env Rscript

# Test Suite 09: Accessibility (a11y), Semantic Landmarks & Structure Audit
base_url <- "https://staging.join-ecotopia.org"

routes <- c(
  "/",
  "/reign",
  "/ministries",
  "/apply",
  "/sign-in",
  "/citizen",
  "/governors",
  "/creators",
  "/terms",
  "/privacy"
)

cat("=== [TEST 09] ACCESSIBILITY (A11Y) & SEMANTIC STRUCTURE AUDIT ===\n")

results <- list()

for (r in routes) {
  url <- paste0(base_url, r)
  cmd <- sprintf("curl -s '%s'", url)
  html <- paste(system(cmd, intern = TRUE), collapse = " ")
  
  has_lang <- grepl('<html[^>]+lang=["\']en["\']', html, ignore.case = TRUE)
  has_viewport <- grepl('<meta[^>]+viewport', html, ignore.case = TRUE)
  has_main <- grepl('<main', html, ignore.case = TRUE)
  has_h1 <- grepl('<h1', html, ignore.case = TRUE)
  has_footer <- grepl('<footer', html, ignore.case = TRUE)
  
  # Image alt tag check: find all img tags, check if all have alt
  img_matches <- gregexpr('<img[^>]*>', html, ignore.case = TRUE)[[1]]
  if (img_matches[1] != -1) {
    img_tags <- regmatches(html, list(img_matches))[[1]]
    missing_alt <- sum(!grepl('alt=["\'][^"\']*["\']', img_tags, ignore.case = TRUE))
  } else {
    missing_alt <- 0
  }
  
  score <- sum(c(has_lang, has_viewport, has_main, has_h1, has_footer))
  verdict <- ifelse(score >= 4 && missing_alt == 0, "PASS", ifelse(score >= 3, "WARN", "FAIL"))
  
  results[[r]] <- data.frame(
    Route = r,
    Lang_Attr = ifelse(has_lang, "PASS", "FAIL"),
    Viewport = ifelse(has_viewport, "PASS", "FAIL"),
    Main_Tag = ifelse(has_main, "YES", "NO"),
    H1_Heading = ifelse(has_h1, "YES", "NO"),
    Footer_Tag = ifelse(has_footer, "YES", "NO"),
    Missing_Alts = missing_alt,
    Verdict = verdict,
    strings_as_factors = FALSE
  )
}

df_res <- do.call(rbind, results)
print(df_res, row.names = FALSE)

pass_count <- sum(df_res$Verdict == "PASS")
total_count <- nrow(df_res)
cat(sprintf("\nAccessibility Summary: %d / %d routes meet semantic HTML standards (%.1f%%)\n\n", pass_count, total_count, (pass_count/total_count)*100))
