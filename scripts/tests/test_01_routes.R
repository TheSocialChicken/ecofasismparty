#!/usr/bin/env Rscript

# Test Suite 01: Route Availability, HTTP Status Codes & Latency
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

cat("=== [TEST 01] ROUTE AVAILABILITY & LATENCY AUDIT ===\n")

results <- list()

for (r in routes) {
  url <- paste0(base_url, r)
  cmd <- sprintf("curl -s -o /dev/null -w '%%{http_code} %%{time_total} %%{size_download}' '%s'", url)
  output <- system(cmd, intern = TRUE)
  parts <- strsplit(trimws(output), " ")[[1]]
  status <- as.integer(parts[1])
  time_sec <- as.numeric(parts[2])
  size_bytes <- as.integer(parts[3])
  
  passed <- (status == 200) && (size_bytes > 500)
  verdict <- ifelse(passed, "PASS", "FAIL")
  
  results[[r]] <- data.frame(
    Route = r,
    Status = status,
    Latency_ms = round(time_sec * 1000, 1),
    Size_KB = round(size_bytes / 1024, 1),
    Verdict = verdict,
    strings_as_factors = FALSE
  )
}

df_res <- do.call(rbind, results)
print(df_res, row.names = FALSE)

# Summary
pass_count <- sum(df_res$Verdict == "PASS")
total_count <- nrow(df_res)
cat(sprintf("\nResult: %d / %d routes passed (%.1f%%)\n\n", pass_count, total_count, (pass_count/total_count)*100))
