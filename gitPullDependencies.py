import enterprise.enterpriceDependecies.enterpriceDependecies
from project.projectConfig.projectConfig import projectConfig
from enterprise.enterpriseDeployment.enterpriseDeployment import EnterpriseDeployment

enterpriseDeployment = EnterpriseDeployment()
res = enterpriseDeployment.controller(projectConfig)
print (res)