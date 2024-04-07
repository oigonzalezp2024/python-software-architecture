from git import Repo

class EnterpriseDeployment():

    def clonarRepo(self, git_url:str, repo_dir:str)->str:
        try:
            Repo.clone_from(git_url, repo_dir)  
            return ">>> Repositorios clonados."  
        except Exception as err:
            return str(">>> Repositorios actualizados.\n")

        
    def controller(self, dependecias:object)->str:
        try:
            for dependecia in dependecias:
                git_url = dependecia['git_url']
                repo_dir = dependecia['repo_dir']
                res = self.clonarRepo(git_url, repo_dir)
            return res
        except Exception as err:
            return str(f">>> El directorio: \n{repo_dir}, ya existe\n")
