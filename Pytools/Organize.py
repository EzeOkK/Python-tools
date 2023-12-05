class CodeOrganizer:
    @staticmethod
    def organize_imports(file_content):
        """Organize the imports in a given python code content."""
        
        lines = file_content.strip().split('\n')
        import_lines = sorted([line.strip() for line in lines if line.strip().startswith('import') or line.strip().startswith('from')])
        other_lines = [line.strip() for line in lines if not (line.strip().startswith('import') or line.strip().startswith('from'))]
        
        organized_code = '\n'.join(import_lines) + ('\n\n' if import_lines else '') + '\n'.join(other_lines)
        return organized_code.strip()

    @staticmethod
    def correct_typo_errors(line):
        """Correct common typo errors in python code."""
        corrections = {
            'inport': 'import',
            'fro': 'from',
            'pritn': 'print',
            'defi': 'def',
            'retu': 'return',
            'whil': 'while',
            'forl': 'for',
            'ifel': 'if',
            'els': 'else',
            'thru': 'try',
            'exce': 'except',
            'fina': 'finally',
            'clase': 'class',
            'execept': 'except'
        }
        for typo, correct in corrections.items():
            line = line.replace(typo, correct)
        return line

    @classmethod
    def organize_code_file(cls, file_path):
        """Read a python file, correct typos, organize its imports, and overwrite the file with the organized code."""
        with open(file_path, 'r') as file:
            content = file.read()

        
        lines = content.split('\n')
        corrected_lines = [cls.correct_typo_errors(line) for line in lines]
        corrected_content = '\n'.join(corrected_lines)

        
        organized_content = cls.organize_imports(corrected_content)
        
        with open(file_path, 'w') as file:
            file.write(organized_content)
