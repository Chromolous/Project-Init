
TEMPLATES = {
    "python": {
        "main.py": '''def main():
    print("Hello, World")


if __name__ == "__main__":
    main()
''',
        ".gitignore": """__pycache__/
*.py[cod]
.venv/
venv/
.env
.pytest_cache/
.idea/
.vscode/
dist/
build/
""",
    },

    "javascript": {
        "index.js": '''function main() {
    console.log("Hello, World");
}

main();
''',
        "package.json": """{
  "name": "{{name}}",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  }
}
""",
        ".gitignore": """node_modules/
.env
dist/
coverage/
.vscode/
""",
    },

    "typescript": {
        "src/index.ts": '''function main(): void {
    console.log("Hello, World");
}

main();
''',
        "package.json": """{
  "name": "{{name}}",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "devDependencies": {
    "typescript": "^5.0.0"
  }
}
""",
        "tsconfig.json": """{
  "compilerOptions": {
    "target": "ES2022",
    "module": "CommonJS",
    "rootDir": "src",
    "outDir": "dist",
    "strict": true
  },
  "include": ["src/**/*.ts"]
}
""",
        ".gitignore": """node_modules/
dist/
.env
.vscode/
""",
    },

    "java": {
        "Main.java": '''public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}
''',
        ".gitignore": """*.class
out/
target/
.idea/
.vscode/
.env
""",
    },

    "c": {
        "main.c": '''#include <stdio.h>

int main(void) {
    printf("Hello, World");
    return 0;
}
''',
        ".gitignore": """*.o
*.obj
*.exe
*.out
build/
.vscode/
""",
    },

    "cpp": {
        "main.cpp": '''#include <iostream>

int main() {
    std::cout << "Hello, World";
    return 0;
}
''',
        ".gitignore": """*.o
*.obj
*.exe
*.out
build/
.vscode/
""",
    },
}
