#!/usr/bin/env Rscript

# Test Suite 08: OpenGraph, Social Sharing & SEO Metadata Audit
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

cat("=== [TEST 08] OPENGRAPH & SOCIAL METADATA AUDIT ===\n")

results <- list()

for (r in routes) {
  url <- paste0(base_url, r)
  cmd <- sprintf("curl -s '%s'", url)
  html <- paste(system(cmd, intern = TRUE), collapse = " ")
  
  has_title <- grepl("<title>", html, ignore.case = TRUE)
  has_desc <- grepl('<meta[^>]+name=["\']description["\']', html, ignore.case = TRUE)
  has_og_title <- grepl('<meta[^>]+property=["\']og:title["\']', html, ignore.case = TRUE)
  has_og_desc <- grepl('<meta[^>]+property=["\']og:description["\']', html, ignore.case = TRUE)
  has_og_img <- grepl('<meta[^>]+property=["\']og:image["\']', html, ignore.case = TRUE)
  has_twitter <- grepl('<meta[^>]+name=["\']twitter:card["\']', html, ignore.case = TRUE)
  has_favicon <- grepl('<link[^>]+rel=["\']icon["\']', html, ignore.case = TRUE)
  
  score <- sum(c(has_title, has_desc, has_og_title, has_og_desc, has_og_img, has_twitter, has_favicon))
  verdict <- ifelse(score >= 6, "PASS", ifelse(score >= 4, "WARN", "FAIL"))
  
  results[[r]] <- data.frame(
    Route = r,
    Title = ifelse(has_title, "YES", "NO"),
    Description = ifelse(has_desc, "YES", "NO"),
    OG_Title = ifelse(has_og_title, "YES", "NO"),
    OG_Image = ifelse(has_og_img, "YES", "NO"),
    Twitter_Card = ifelse(has_twitter, "YES", "NO"),
    Favicon = ifelse(has_favicon, "YES", "NO"),
    Score = sprintf("%d/7", score),
    Verdict = verdict,
    strings_as_factors = FALSE
  )
}

df_res <- do.call(rbind, results)
print(df_res, row.names = FALSE)

pass_count <- sum(df_res$Verdict == "PASS")
total_count <- nrow(df_res)
cat(sprintf("\nMetadata Coverage: %d / %d routes have complete social meta tags (%.1f%%)\n\n", pass_count, total_count, (pass_count/total_count)*100))
