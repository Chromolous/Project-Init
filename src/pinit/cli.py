import subprocess
import sys
import questionary
from pinit.generator import create_project

def main():
    languages = {
        "Python": "python",
        "JavaScript": "javascript",
        "TypeScript": "typescript",
        "Java": "java",
        "C": "c",
        "C++": "cpp",
    }
    
    language = questionary.select("Qual linguagem você deseja utilizar?", choices=list(languages.keys())).ask()
    
    if not language:
        print("Operação cancelada.")
        return
    
    name = questionary.text("Qual será o nome do projeto?", validate=lambda value: (True if value.strip() else "O nome do projeto não pode ficar vazio.")).ask()
    
    if not name:
        print("Operação cancelada.")
        return
    
    name = name.strip()
    
    github = questionary.confirm("Deseja publicar o projeto no GitHub?", default=False).ask()
    
    if github is None:
        print("Operação cancelada.")
        return

    public = False
    
    if github:
        public = questionary.confirm("O repositório vai ser público?", default=False).ask()
        if public is None:
            print("Operação cancelada.")
            return
        
    try:
        create_project(languages[language],name,github,public)

        print("Projeto criado com sucesso.")

    except (ValueError, FileExistsError) as error:
        print(f"\nErro: {error}", file=sys.stderr)
        raise SystemExit(1)

    except FileNotFoundError as error:
        print(
            f"\nPrograma externo não encontrado: {error}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    except subprocess.CalledProcessError as error:
        print(
            f"\nUm comando externo falhou "
            f"(código {error.returncode}).",
            file=sys.stderr,
        )
        print(
            "Verifique o Git, o GitHub CLI e a autenticação.",
            file=sys.stderr,
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()