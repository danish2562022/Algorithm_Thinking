#!/usr/bin/env python3
"""
Create student versions of notebooks without solutions.
"""

import json
import re
from pathlib import Path

def is_solution_section(cell):
    """Check if a cell starts a solution section"""
    if cell.get('cell_type') != 'markdown':
        return False
    
    source = ''.join(cell.get('source', []))
    return bool(re.search(r'##\s+Solutions?|###\s+Solution|</?details>', source, re.IGNORECASE))

def is_solution_cell(cell, in_solution_section=False):
    """Check if a cell contains solutions"""
    source = ''.join(cell.get('source', []))
    
    # Markdown cells with solution indicators
    if cell.get('cell_type') == 'markdown':
        if is_solution_section(cell):
            return True
        if '</details>' in source or '<details>' in source:
            return True
        if re.search(r'###\s+Solution\s+\d+', source, re.IGNORECASE):
            return True
    
    # Code cells with solution implementations
    if cell.get('cell_type') == 'code' and in_solution_section:
        # Check for solution function definitions (but not TODO exercises)
        if '# TODO' in source or '# Your solution' in source:
            return False  # This is an exercise, not a solution
        if re.search(r'def\s+(find_min|sum_even|reverse_list|is_sorted|is_anagram|contains_duplicate|max_profit)', source):
            # Check if it's actually a solution (no TODO)
            if '# Solution' in source or '# Answer' in source:
                return True
            # If we're in solution section and it's a complete function, it's likely a solution
            if 'pass' not in source and 'TODO' not in source:
                return True
    
    return False

def create_student_notebook_from_existing(notebook_path):
    """Create student version from existing notebook"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    student_cells = []
    in_solution_section = False
    
    for cell in notebook['cells']:
        source = ''.join(cell.get('source', []))
        
        # Check for solution section markers
        if is_solution_section(cell):
            in_solution_section = True
            student_cells.append({
                'cell_type': 'markdown',
                'metadata': {},
                'source': [
                    '## Practice Time!\n',
                    '\n',
                    '**Great work!** Try to solve the exercises above on your own.\n',
                    'When ready, check solutions in the original notebook or ask your instructor.'
                ]
            })
            continue
        
        # Handle solution section
        if in_solution_section:
            if '</details>' in source or (cell.get('cell_type') == 'markdown' and re.match(r'^##\s+[^#]', source) and 'Solution' not in source):
                in_solution_section = False
        
        # Skip solution cells
        if in_solution_section and is_solution_cell(cell, True):
            continue
        
        # Skip standalone solution cells
        if not in_solution_section and is_solution_cell(cell, False):
            continue
        
        student_cells.append(cell)
    
    return {
        'cells': student_cells,
        'metadata': notebook['metadata'],
        'nbformat': notebook['nbformat'],
        'nbformat_minor': notebook['nbformat_minor']
    }

def main():
    """Create student notebooks"""
    tutorial_dir = Path(__file__).parent
    
    # Remove old student notebooks
    for old_nb in tutorial_dir.glob('*_student.ipynb'):
        old_nb.unlink()
    
    # Process existing notebooks
    notebook_files = sorted([f for f in tutorial_dir.glob('tutorial_*.ipynb') 
                            if '_student' not in f.name])
    
    print(f"Creating student versions of {len(notebook_files)} notebooks...\n")
    
    for notebook_path in notebook_files:
        print(f"Processing {notebook_path.name}...", end=' ')
        
        try:
            student_notebook = create_student_notebook_from_existing(notebook_path)
            
            student_filename = notebook_path.stem + '_student.ipynb'
            student_path = tutorial_dir / student_filename
            
            with open(student_path, 'w', encoding='utf-8') as f:
                json.dump(student_notebook, f, indent=1, ensure_ascii=False)
            
            original_cells = len(json.load(open(notebook_path))['cells'])
            student_cells = len(student_notebook['cells'])
            removed = original_cells - student_cells
            
            print(f"✓ ({removed} solution cells removed)")
            
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print("✓ Student notebooks created successfully!")
    print("\nStudent versions (no solutions):")
    for nb in sorted(tutorial_dir.glob('*_student.ipynb')):
        print(f"  - {nb.name}")

if __name__ == "__main__":
    main()
