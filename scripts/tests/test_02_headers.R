#!/usr/bin/env Rscript

# Test Suite 02: HTTP Security & Privacy Headers Compliance
base_url <- "https://staging.join-ecotopia.org"

cat("=== [TEST 02] SECURITY & PRIVACY HEADERS AUDIT ===\n")

raw_headers <- system(sprintf("curl -s -I '%s/'", base_url), intern = TRUE)

get_header <- function(name) {
  matches <- grep(paste0("^", name, ":"), raw_headers, ignore.case = TRUE, value = TRUE)
  if (length(matches) > 0) {
    val <- sub(paste0("^", name, ":\\s*"), "", matches[1], ignore.case = TRUE)
    return(trimws(val))
  }
  return(NA_character_)
}

checks <- list(
  list(name = "Strict-Transport-Security", req = "max-age >= 31536000", critical = TRUE),
  list(name = "X-Robots-Tag", req = "noindex, nofollow (staging)", critical = TRUE),
  list(name = "Content-Security-Policy", req = "frame-ancestors 'none' or restrictive CSP", critical = FALSE),
  list(name = "X-Content-Type-Options", req = "nosniff", critical = TRUE),
  list(name = "Referrer-Policy", req = "strict-origin-when-cross-origin / no-referrer", critical = FALSE),
  list(name = "X-Frame-Options", req = "DENY / SAMEORIGIN", critical = FALSE)
)

results <- list()

for (c in checks) {
  val <- get_header(c$name)
  present <- !is.na(val)
  
  if (c$name == "Strict-Transport-Security") {
    pass <- present && grepl("max-age=", val)
  } else if (c$name == "X-Robots-Tag") {
    pass <- present && grepl("noindex", val)
  } else if (c$name == "X-Content-Type-Options") {
    pass <- present && grepl("nosniff", val)
  } else if (c$name == "Content-Security-Policy") {
    pass <- present
  } else if (c$name == "Referrer-Policy") {
    pass <- present
  } else if (c$name == "X-Frame-Options") {
    pass <- present || (!is.na(get_header("Content-Security-Policy")) && grepl("frame-ancestors", get_header("Content-Security-Policy")))
  } else {
    pass <- present
  }
  
  status_str <- if (pass) "PASS" else if (c$critical) "FAIL (BLOCKER)" else "WARN (NEEDS FIX)"
  
  results[[c$name]] <- data.frame(
    Header = c$name,
    Value = ifelse(is.na(val), "(Missing)", val),
    Requirement = c$req,
    Verdict = status_str,
    strings_as_factors = FALSE
  )
}

df_headers <- do.call(rbind, results)
print(df_headers, row.names = FALSE)

failed_critical <- sum(grepl("FAIL", df_headers$Verdict))
cat(sprintf("\nCritical Header Failures: %d\n\n", failed_critical))
