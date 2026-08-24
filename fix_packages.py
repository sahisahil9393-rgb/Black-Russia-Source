#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Black Russia Source - Package Fix Script
Place this file in the ROOT of your project (where settings.gradle is)
Run: python3 fix_packages.py
It will automatically fix ALL Java files, build.gradle, and AndroidManifest.xml
"""

import os
import sys

def fix_all_files():
    project_root = os.path.dirname(os.path.abspath(__file__))
    java_dir = os.path.join(project_root, "app", "src", "main", "java")
    build_gradle = os.path.join(project_root, "app", "build.gradle")
    manifest = os.path.join(project_root, "app", "src", "main", "AndroidManifest.xml")

    fixed_count = 0
    errors = []

    # Fix all .java files
    if os.path.exists(java_dir):
        for root, dirs, files in os.walk(java_dir):
            for file in files:
                if file.endswith(".java"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                        original = content

                        # 1. Fix all package declarations and imports
                        content = content.replace("com.byparad1st", "com.Parad1st")

                        # 2. Fix GTASA class reference (remove .core if pointing to root GTASA)
                        content = content.replace("com.Parad1st.game.core.GTASA", "com.Parad1st.game.GTASA")

                        if content != original:
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(content)
                            rel_path = os.path.relpath(filepath, project_root)
                            print(f"[FIXED] {rel_path}")
                            fixed_count += 1
                    except Exception as e:
                        errors.append(f"Error in {filepath}: {e}")
    else:
        print("[WARNING] Java directory not found:", java_dir)

    # Fix build.gradle
    if os.path.exists(build_gradle):
        try:
            with open(build_gradle, "r", encoding="utf-8") as f:
                content = f.read()
            original = content
            content = content.replace("com.byparad1st", "com.Parad1st")
            content = content.replace("applicationId 'com.Parad1stgames.game'", "applicationId 'com.Parad1st.game'")
            content = content.replace('applicationId "com.Parad1stgames.game"', "applicationId 'com.Parad1st.game'")
            if content != original:
                with open(build_gradle, "w", encoding="utf-8") as f:
                    f.write(content)
                print("[FIXED] app/build.gradle")
                fixed_count += 1
        except Exception as e:
            errors.append(f"Error in build.gradle: {e}")
    else:
        print("[WARNING] build.gradle not found")

    # Fix AndroidManifest.xml
    if os.path.exists(manifest):
        try:
            with open(manifest, "r", encoding="utf-8") as f:
                content = f.read()
            original = content
            content = content.replace("com.byparad1st", "com.Parad1st")
            content = content.replace("com.Parad1st.game.core.GTASA", "com.Parad1st.game.GTASA")
            if content != original:
                with open(manifest, "w", encoding="utf-8") as f:
                    f.write(content)
                print("[FIXED] AndroidManifest.xml")
                fixed_count += 1
        except Exception as e:
            errors.append(f"Error in AndroidManifest.xml: {e}")
    else:
        print("[WARNING] AndroidManifest.xml not found")

    print(f"\n{'='*50}")
    print(f"Total files fixed: {fixed_count}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  - {e}")
    else:
        print("No errors!")
    print(f"{'='*50}")
    print("\nNext steps:")
    print("  1. In Android Studio: File -> Invalidate Caches / Restart")
    print("  2. Then: Build -> Rebuild Project")
    print("  3. Or push to GitHub and let Actions build it automatically")

if __name__ == "__main__":
    fix_all_files()
