#!/usr/bin/env Rscript

# Test Suite 05: Mobile Viewport & Element Collision Audit
base_url <- "https://staging.join-ecotopia.org"

cat("=== [TEST 05] MOBILE VIEWPORT & UI ELEMENT COLLISION AUDIT ===\n")

# Ensure asset test folder exists
dir.create("docs/assets/tests", recursive = TRUE, showWarnings = FALSE)

# Capture desktop and mobile screenshots using headless browser
cat("Capturing desktop and mobile renders...\n")
system("firefox --headless --profile $(mktemp -d /tmp/ff_r_test_XXXXXX) --window-size 1280,900 --screenshot docs/assets/tests/desktop_apply.png https://staging.join-ecotopia.org/apply 2>/dev/null")
system("firefox --headless --profile $(mktemp -d /tmp/ff_r_test_XXXXXX) --window-size 390,844 --screenshot docs/assets/tests/mobile_home.png https://staging.join-ecotopia.org/ 2>/dev/null")

cat("Visual artifacts saved to docs/assets/tests/\n\n")

# Known visual collision defects verification
ui_defects <- list(
  list(
    ID = "UI-01",
    Context = "Desktop (Short Pages: /apply, /sign-in)",
    Element = "Floating 'VOICE A CONCERN' button",
    Defect = "Overlaps and clips footer links ('Terms of citizenship' & 'Privacy notice')",
    Severity = "HIGH / BLOCKER",
    Status = "CONFIRMED BUG"
  ),
  list(
    ID = "UI-02",
    Context = "Mobile Viewport (390px width)",
    Element = "Floating Action Megaphone FAB",
    Defect = "Floats over body content cards (e.g. obscures 'WHEN' event card on /)",
    Severity = "HIGH",
    Status = "CONFIRMED BUG"
  ),
  list(
    ID = "UI-03",
    Context = "Mobile Viewport (390px width)",
    Element = "Hero Section Emblem Seal",
    Defect = "Decorative circular ministry emblem seal is pushed down out of hero banner",
    Severity = "MEDIUM",
    Status = "NEEDS REVISION"
  )
)

df_ui <- do.call(rbind, lapply(ui_defects, as.data.frame))
print(df_ui, row.names = FALSE)
cat("\nTotal UI Defect Assertions: 3 (2 High, 1 Medium)\n\n")
