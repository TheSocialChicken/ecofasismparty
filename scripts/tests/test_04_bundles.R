#!/usr/bin/env Rscript

# Test Suite 04: Bundle Integrity, Anti-AI Irony & Privacy Audit
base_url <- "https://staging.join-ecotopia.org"

cat("=== [TEST 04] BUNDLE ASSETS, AI DECREE & TRACKING AUDIT ===\n")

# Get JS chunks loaded on /apply
html <- system(sprintf("curl -s '%s/apply'", base_url), intern = TRUE)
full_html <- paste(html, collapse = " ")

# Extract chunk URLs
chunk_paths <- unique(regmatches(full_html, gregexpr("/_next/static/immutable/chunks/[a-zA-Z0-9_\\.-]+\\.js", full_html))[[1]])
css_paths <- unique(regmatches(full_html, gregexpr("/_next/static/immutable/chunks/[a-zA-Z0-9_\\.-]+\\.css", full_html))[[1]])

cat(sprintf("Discovered %d JS chunks and %d CSS stylesheets on /apply\n", length(chunk_paths), length(css_paths)))

# Verify all return HTTP 200
asset_failures <- 0
for (cp in c(chunk_paths, css_paths)) {
  status <- as.integer(system(sprintf("curl -s -o /dev/null -w '%%{http_code}' '%s%s'", base_url, cp), intern = TRUE))
  if (status != 200) {
    cat(sprintf("Asset failure: %s -> HTTP %d\n", cp, status))
    asset_failures <- asset_failures + 1
  }
}

cat("Asset Delivery Health:", ifelse(asset_failures == 0, "100% OK (All return HTTP 200)", paste(asset_failures, "Assets failed")), "\n\n")

# Scan chunks for forbidden AI dependencies
cat("Auditing for Banned AI Dependencies vs. Public R.E.I.G.N. Decree...\n")
ai_found <- FALSE
ai_details <- c()

posthog_found <- FALSE
posthog_details <- c()

for (cp in chunk_paths) {
  content <- system(sprintf("curl -s '%s%s'", base_url, cp), intern = TRUE)
  blob <- paste(content, collapse = " ")
  
  if (grepl("anthropic", blob, ignore.case = TRUE) || grepl("/v1/messages", blob)) {
    ai_found <- TRUE
    ai_details <- c(ai_details, cp)
  }
  if (grepl("posthog", blob, ignore.case = TRUE)) {
    posthog_found <- TRUE
    posthog_details <- c(posthog_details, cp)
  }
}

cat(" - Official Public Stance: 'By decree of R.E.I.G.N., artificial intelligence is banned'\n")
cat(" - AI Client SDK in Frontend Bundle:", ifelse(ai_found, "FLAGGED (Anthropic SDK code detected)", "Clean"), "\n")
if (ai_found) cat(sprintf("   Chunks containing AI refs: %s\n", paste(ai_details, collapse = ", ")))

cat("\nAuditing for Third-Party Analytics vs. Public Privacy Notice...\n")
cat(" - Official Privacy Notice: 'There are no analytics, tracking, advertising or third-party cookies'\n")
cat(" - PostHog Analytics Client in Bundle:", ifelse(posthog_found, "FLAGGED (PostHog tracking code detected)", "Clean"), "\n")
if (posthog_found) cat(sprintf("   Chunks containing PostHog refs: %s\n", paste(posthog_details, collapse = ", ")))
cat("\n")
