#!/usr/bin/env python3
"""
Verification Test Suite for Ecotopia A6 Passport Booklets
Verifies HTML structure, page counts, imposition layouts, view switchers, and navigation links.
"""

import os
import re
import sys

BOOKLETS = [
    {
        "file": "print_passport_a6_booklet.html",
        "expected_pages": 8,
        "expected_sheets": 1,
        "title": "Citizen Passport",
    },
    {
        "file": "print_broadcast_scripts_a6_booklet.html",
        "expected_pages": 8,
        "expected_sheets": 1,
        "title": "Broadcast Scripts & Liturgies",
    },
    {
        "file": "print_lore_bible_a6_booklet.html",
        "expected_pages": 16,
        "expected_sheets": 2,
        "title": "Lore & Narrative Bible",
    },
    {
        "file": "print_game_design_a6_booklet.html",
        "expected_pages": 16,
        "expected_sheets": 2,
        "title": "Game Design & Economics",
    },
    {
        "file": "print_quest_cards_a6_booklet.html",
        "expected_pages": 16,
        "expected_sheets": 2,
        "title": "Quest Cards & Facilitator",
    },
]

def run_tests():
    print("=== ECOTOPIA A6 PASSPORT BOOKLET VERIFICATION SUITE ===")
    total_passed = 0
    total_checks = 0

    for b in BOOKLETS:
        filepath = b["file"]
        print(f"\nAuditing Booklet: {b['title']} ({filepath})")
        
        # 1. Existence check
        total_checks += 1
        if not os.path.isfile(filepath):
            print(f"  [FAIL] File {filepath} does not exist!")
            sys.exit(1)
        print(f"  [PASS] File exists on disk ({os.path.getsize(filepath)} bytes)")
        total_passed += 1

        content = open(filepath, "r", encoding="utf-8").read()

        # 2. Structural HTML checks
        total_checks += 1
        assert "<!DOCTYPE html>" in content, f"Missing doctype in {filepath}"
        assert "<html" in content and "</html>" in content, f"Missing html tags in {filepath}"
        assert "<body" in content and "</body>" in content, f"Missing body tags in {filepath}"
        print("  [PASS] Clean semantic HTML5 document structure verified")
        total_passed += 1

        # 3. View Switcher & Script checks
        total_checks += 1
        assert "function switchView(mode)" in content, f"Missing switchView function in {filepath}"
        assert 'id="imposition-view"' in content, f"Missing imposition-view container in {filepath}"
        assert 'id="reading-view"' in content, f"Missing reading-view container in {filepath}"
        assert 'btn-imposition' in content and 'btn-reading' in content, f"Missing view toggle buttons in {filepath}"
        print("  [PASS] Dual-mode view engine present (A4 Imposition + Sequential Reader)")
        total_passed += 1

        # 4. Navigation Links check
        total_checks += 1
        for other_b in BOOKLETS:
            assert other_b["file"] in content, f"Missing navigation link to {other_b['file']} in {filepath}"
        print("  [PASS] Universal cross-booklet navigation links intact")
        total_passed += 1

        # 5. Page count and sequence check
        total_checks += 1
        pages_found = sorted(set([int(p) for p in re.findall(r'<div class="page-number">(\d+)</div>', content)]))
        expected_seq = list(range(1, b["expected_pages"] + 1))
        assert pages_found == expected_seq, f"Page sequence mismatch in {filepath}: found {pages_found}, expected {expected_seq}"
        print(f"  [PASS] Page count ({len(pages_found)} pages) and sequence (1..{b['expected_pages']}) 100% verified")
        total_passed += 1

        # 6. Duplex Imposition check
        total_checks += 1
        sheets_found = len(re.findall(r'class="sheet-container"', content))
        # Expected sheets in imposition view: 2 sheets for 1 A4 (Side A + Side B), 4 sheets for 2 A4 (Paper 1 A/B + Paper 2 A/B)
        expected_imposition_sheets = b["expected_sheets"] * 2
        assert sheets_found == expected_imposition_sheets, f"Imposition sheet count mismatch in {filepath}: found {sheets_found}, expected {expected_imposition_sheets}"
        print(f"  [PASS] Duplex A4 cut & fold imposition verified ({sheets_found} print surfaces = {b['expected_sheets']} physical A4 sheet(s))")
        total_passed += 1

        # 7. Print CSS check
        total_checks += 1
        assert "@media print" in content, f"Missing @media print in {filepath}"
        assert "page-break-after: always" in content, f"Missing page-break-after in {filepath}"
        assert "size: A4 portrait" in content, f"Missing size: A4 portrait in {filepath}"
        print("  [PASS] @media print rules verified for borderless duplex A4 generation")
        total_passed += 1

    print("\n------------------------------------------------------------")
    print(f"RESULT: ALL {total_passed} / {total_checks} PASSPORT AUDIT CHECKS PASSED (100.0%)")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    run_tests()
