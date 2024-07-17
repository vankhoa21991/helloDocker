# helloDocker
creating a test docker image 

checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vankhoa21991/helloDocker']])

withCredentials([string(credentialsId: 'docker_hub', variable: 'docker_hub')]) {
    // some block
}

kubernetesDeploy configs: '', kubeConfig: [path: ''], kubeconfigId: 'kubeconfig', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']