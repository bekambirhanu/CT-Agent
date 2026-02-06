#!/usr/bin/env python3
"""Test script to debug import issues"""

print("Step 1: Testing basic import...")
try:
    import shared
    print(f"✅ shared module found at: {shared.__file__}")
except Exception as e:
    print(f"❌ Failed to import shared: {e}")
    exit(1)

print("\nStep 2: Testing shared.shared import...")
try:
    import shared.shared
    print(f"✅ shared.shared module found")
except Exception as e:
    print(f"❌ Failed to import shared.shared: {e}")
    exit(1)

print("\nStep 3: Testing shared.shared.config import...")
try:
    import shared.shared.config
    print(f"✅ shared.shared.config module found")
except Exception as e:
    print(f"❌ Failed to import shared.shared.config: {e}")
    exit(1)

print("\nStep 4: Testing Settings import (this might hang)...")
try:
    from shared.shared.config.Settings import Settings
    print(f"✅ Settings imported successfully!")
    print(f"   TELEGRAM_BOT_TOKEN: {Settings.TELEGRAM_BOT_TOKEN[:15]}...")
except Exception as e:
    print(f"❌ Failed to import Settings: {e}")
    exit(1)

print("\n✅ All imports successful!")
