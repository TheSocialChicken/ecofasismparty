#!/usr/bin/env Rscript

# Test Suite 07: Concurrency, TTFB & Burst Latency Benchmark
base_url <- "https://staging.join-ecotopia.org"

cat("=== [TEST 07] CONCURRENCY & BURST LATENCY PERFORMANCE BENCHMARK ===\n")

target_routes <- c("/", "/ministries", "/citizen", "/apply")
samples_per_route <- 10

results <- list()

for (r in target_routes) {
  url <- paste0(base_url, r)
  latencies <- numeric(samples_per_route)
  ttfb_list <- numeric(samples_per_route)
  
  for (i in 1:samples_per_route) {
    cmd <- sprintf("curl -s -o /dev/null -w '%%{time_starttransfer} %%{time_total}' '%s'", url)
    out <- system(cmd, intern = TRUE)
    parts <- strsplit(trimws(out), " ")[[1]]
    ttfb_list[i] <- as.numeric(parts[1]) * 1000
    latencies[i] <- as.numeric(parts[2]) * 1000
  }
  
  min_lat <- round(min(latencies), 1)
  med_lat <- round(median(latencies), 1)
  mean_lat <- round(mean(latencies), 1)
  p95_lat <- round(quantile(latencies, 0.95), 1)
  max_lat <- round(max(latencies), 1)
  mean_ttfb <- round(mean(ttfb_list), 1)
  
  # Door SLA: P95 should be under 800ms for smooth garage check-in
  verdict <- ifelse(p95_lat < 800, "PASS (Optimal)", ifelse(p95_lat < 1500, "WARN (Acceptable)", "FAIL (Slow)"))
  
  results[[r]] <- data.frame(
    Route = r,
    Samples = samples_per_route,
    Mean_TTFB_ms = mean_ttfb,
    Min_ms = min_lat,
    Median_ms = med_lat,
    Mean_ms = mean_lat,
    P95_ms = p95_lat,
    Max_ms = max_lat,
    SLA_Verdict = verdict,
    strings_as_factors = FALSE
  )
}

df_res <- do.call(rbind, results)
print(df_res, row.names = FALSE)

optimal_count <- sum(grepl("PASS", df_res$SLA_Verdict))
total_count <- nrow(df_res)
cat(sprintf("\nPerformance Summary: %d / %d audited routes meet garage door SLA (<800ms P95)\n\n", optimal_count, total_count))
