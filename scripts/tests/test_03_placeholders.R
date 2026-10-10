#!/usr/bin/env Rscript

# Test Suite 03: Legal & Content Placeholders Scan (Gate E Compliance)
base_url <- "https://staging.join-ecotopia.org"

pages_to_scan <- c("/terms", "/privacy", "/apply", "/sign-in", "/citizen", "/")

cat("=== [TEST 03] UNRESOLVED DRAFT & PLACEHOLDER AUDIT ===\n")

findings <- list()

for (p in pages_to_scan) {
  url <- paste0(base_url, p)
  cmd <- sprintf("curl -s '%s' | grep -oi '\\[\\(placeholder\\|draft\\)[^]]*\\]' | sort -u", url)
  matches <- system(cmd, intern = TRUE)
  
  if (length(matches) > 0) {
    clean_matches <- unique(trimws(matches))
    clean_matches <- clean_matches[nchar(clean_matches) > 0]
    
    for (m in clean_matches) {
      m_clean <- gsub("&x27;", "'", m)
      m_clean <- gsub("&#x27;", "'", m_clean)
      m_clean <- gsub("\\\\\"", "", m_clean)
      
      cat_name <- if (grepl("pay|amount|donation", m_clean, ignore.case = TRUE)) "Pricing / Finance"
                  else if (grepl("house rules|age|step out", m_clean, ignore.case = TRUE)) "Safety / Game Rules"
                  else if (grepl("organiser|contact", m_clean, ignore.case = TRUE)) "Legal Identity"
                  else if (grepl("legal basis", m_clean, ignore.case = TRUE)) "GDPR Compliance"
                  else if (grepl("backup", m_clean, ignore.case = TRUE)) "Data Retention"
                  else "General Content"
                  
      owner <- if (cat_name %in% c("Pricing / Finance", "Legal Identity")) "Jack"
               else if (cat_name == "Safety / Game Rules") "Chris / Safety Lead"
               else "Tech Team"
               
      findings[[length(findings) + 1]] <- data.frame(
        Page = p,
        Category = cat_name,
        Placeholder = m_clean,
        Owner = owner,
        Status = "BLOCKER (UNRESOLVED)",
        strings_as_factors = FALSE
      )
    }
  }
}

if (length(findings) > 0) {
  df_placeholders <- do.call(rbind, findings)
  df_placeholders <- unique(df_placeholders)
  print(df_placeholders, row.names = FALSE)
  cat(sprintf("\nTotal Unresolved Gate E Placeholders: %d (ALL ARE LAUNCH BLOCKERS)\n\n", nrow(df_placeholders)))
} else {
  cat("\nAll placeholders resolved! Clean bill of health.\n\n")
}
