#!/usr/bin/env python3
"""
Create student versions of markdown files without solutions.
"""

import re
from pathlib import Path

def remove_solutions_from_markdown(md_content):
    """Remove solution sections from markdown content"""
    lines = md_content.split('\n')
    result_lines = []
    in_solution_section = False
    in_details_tag = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for solution section start
        if re.match(r'^##\s+Solutions?', line, re.IGNORECASE):
            in_solution_section = True
            # Add encouragement message instead
            result_lines.append('## Practice Time!')
            result_lines.append('')
            result_lines.append('**Great work!** You\'ve reached the practice exercises.')
            result_lines.append('')
            result_lines.append('Try to solve the problems above on your own before checking solutions.')
            result_lines.append('When you\'re ready, you can:')
            result_lines.append('- Check the solutions in the original markdown file')
            result_lines.append('- Ask your instructor for help')
            result_lines.append('- Discuss with classmates')
            result_lines.append('')
            result_lines.append('Remember: The process of solving is more important than getting the answer immediately!')
            result_lines.append('')
            i += 1
            continue
        
        # Check for details tag (collapsible solution sections)
        if '<details>' in line:
            in_details_tag = True
            i += 1
            continue
        
        if '</details>' in line:
            in_details_tag = False
            i += 1
            continue
        
        # Skip solution content
        if in_solution_section or in_details_tag:
            # Check if we're leaving solution section (new major heading)
            if re.match(r'^##\s+[^#]', line) and 'Solution' not in line:
                in_solution_section = False
                in_details_tag = False
                # Continue processing this line
            else:
                # Skip solution lines
                i += 1
                continue
        
        # Check for solution subheadings
        if re.match(r'^###\s+Solution\s+\d+', line, re.IGNORECASE):
            i += 1
            continue
        
        result_lines.append(line)
        i += 1
    
    return '\n'.join(result_lines)

def create_student_markdown(md_file):
    """Create student version of markdown file"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    student_content = remove_solutions_from_markdown(md_content)
    
    return student_content

def main():
    """Create student versions of all markdown files"""
    tutorial_dir = Path(__file__).parent
    
    # Find all tutorial markdown files (exclude README and student versions)
    md_files = sorted([f for f in tutorial_dir.glob('tutorial_*.md') 
                      if '_student' not in f.name])
    
    print(f"Found {len(md_files)} markdown files to process\n")
    
    for md_file in md_files:
        print(f"Processing {md_file.name}...", end=' ')
        
        try:
            student_content = create_student_markdown(md_file)
            
            # Create student version filename
            student_filename = md_file.stem + '_student.md'
            student_path = tutorial_dir / student_filename
            
            # Write student markdown
            with open(student_path, 'w', encoding='utf-8') as f:
                f.write(student_content)
            
            # Count removed lines (approximate)
            original_lines = len(open(md_file).readlines())
            student_lines = len(student_content.split('\n'))
            removed = original_lines - student_lines
            
            print(f"✓ Created {student_filename} ({removed} lines removed)")
            
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print("✓ Student markdown files created successfully!")
    print("\nStudent versions (no solutions):")
    for md in sorted(tutorial_dir.glob('*_student.md')):
        print(f"  - {md.name}")
    print("\nNote: Student markdown files contain exercises but no solutions.")
    print("Students should complete exercises before checking solutions in original files.")

if __name__ == "__main__":
    main()
