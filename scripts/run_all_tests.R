#!/usr/bin/env Rscript

# Master Test Runner for Ecotopia Technical Audit (Suites 01 to 10)
cat("\n============================================================\n")
cat("STARTING ECOTOPIA MASTER TECHNICAL TEST SUITE (R 4.6.1)\n")
cat("Target Environment: https://staging.join-ecotopia.org\n")
cat("============================================================\n\n")

start_time <- Sys.time()

suites <- c(
  "test_01_routes.R",
  "test_02_headers.R",
  "test_03_placeholders.R",
  "test_04_bundles.R",
  "test_05_ui_mobile.R",
  "test_06_intake_validation.R",
  "test_07_performance_load.R",
  "test_08_metadata_og.R",
  "test_09_accessibility_contrast.R",
  "test_10_security_leaks.R"
)

for (s in suites) {
  script_path <- file.path("./scripts/tests", s)
  if (file.exists(script_path)) {
    cat(sprintf(">>> RUNNING %s <<<\n", s))
    system(script_path)
    cat("------------------------------------------------------------\n")
  } else {
    cat(sprintf("[SKIP] File not found: %s\n", script_path))
  }
}

end_time <- Sys.time()
elapsed <- round(as.numeric(difftime(end_time, start_time, units = "secs")), 2)

cat("============================================================\n")
cat(sprintf("ALL 10 TEST SUITES COMPLETED IN %.2f SECONDS\n", elapsed))
cat("============================================================\n\n")
