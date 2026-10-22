import re
import subprocess
from pathlib import Path

from pinit.templates import TEMPLATES

def create_project(linguagem:str, nome:str, github:bool = False, public:bool = False):
    """
    Cria um projeto a partir de um template.

    Args:
        linguagem (str): Linguagem de programação do projeto
        nome (str): Nome do projeto
        github (bool, optional): O projeto vai ser registrado no github? Defaults to False.
        public (bool, optional): O projeto vai ser público? Defaults to False.
    """
    
    if linguagem not in TEMPLATES:
        raise ValueError(f"Linguagem não suportada: {linguagem}")
    
    if not re.fullmatch(r"[A-Za-z0-9_-]+", nome): #evita de criar nomes que o windows não aceite
        raise ValueError("Escolha um nome válido. Use apenas letras, números, hífens e underlines no nome.")
    
    project_dir = Path.cwd() / nome
    
    if project_dir.exists():
        raise FileExistsError(f"O projeto '{nome}' já existe no caminho '{project_dir}'")
    
    project_dir.mkdir()
    
    try:
        files = TEMPLATES[linguagem]
        
        for arquivo, conteudo in files.items():
            conteudo = conteudo.replace("{{name}}", nome)
            file_path = project_dir / arquivo
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(conteudo, encoding="utf-8")
            
        readme = (f"# {nome}\n\n" f"Projeto iniciado com o pinit :D\n\n" f"Linguagem: {linguagem}\n\n" "github.com/Chromolous")
        readme_file = project_dir / "README.md"
        readme_file.write_text(readme, encoding="utf-8")
        
        print(f"Arquivos criados: {project_dir} ...")
        
        subprocess.run(["git", "init", "-b", "main", str(project_dir)], check=True)
        
        print("Git inicializado ...")
        
        if github: # Se o projeto for publicado no github já faz o commit inicial e cria o repositório
            subprocess.run(["git", "add", "."], cwd=project_dir, check=True)
            subprocess.run(["git", "commit", "-m", "Commit inicial"], cwd=project_dir, check=True)
            
            visibility = "--public" if public else "--private"
            
            subprocess.run(["gh", "repo", "create", nome, visibility, "--source", ".", "--remote", "origin", "--push"], cwd=project_dir, check=True)
            
            print("Projeto publicado no GitHub ...")
        
        return project_dir
    
    except Exception as e:
        # Se der algum problema na hora de criar apaga a pasta do projeto que foi criada
        import shutil
        shutil.rmtree(project_dir, ignore_errors=True)
        print("Erro... Limpando mudanças")
        raise e