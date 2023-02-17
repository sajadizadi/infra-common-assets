import yaml
import sys
import json

def fixKubernetesYamls(image, repoName, branchName):
    with open("deployment.yaml") as f_deployment:
        deployment = yaml.safe_load(f_deployment)
        print(deployment["metadata"])
        deployment["metadata"] = {
            "name": repoName,
            "namespace": branchName,
            "labels": {"app": repoName}
        }
        deployment["spec"]["selector"] = {"matchLabels": {"app": repoName}}

        deployment["spec"]["template"]["spec"]["containers"][0]["name"] = repoName
        deployment["spec"]["template"]["spec"]["containers"][0]["image"] = image
        print(yaml.dump(deployment, default_flow_style=False, sort_keys=False))
