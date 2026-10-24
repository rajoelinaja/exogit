"""Tests du module calcul. Lance : python3 src/test_calcul.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calcul import adapter, doubler, total  # noqa: E402

assert doubler(100) == 200, "doubler est faux"
assert adapter(200, 4, 2) == 100, "adapter est faux"
assert total([100, 150, 200]) == 450, "total est faux"

print("Tous les tests passent ✅")
