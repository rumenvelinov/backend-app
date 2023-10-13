pipeline {
    agent any

    stages {
        stage('Installing Helm') {
            steps {
                script {
                    sh '''
                        curl -O https://get.helm.sh/helm-v3.13.1-linux-amd64.tar.gz
                        tar -xzvf helm-v3.13.1-linux-amd64.tar.gz
                        ./linux-amd64/helm version
                    '''
                }
            }
        }

        stage('Deploy Backend') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId:'DB_CREDENTIALS', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "./linux-amd64/helm install --set dbConfig.password=${PASSWORD},dbConfig.user=${USERNAME} backend ./helm/backend"                      
                    }
                }
            }
        }
    }
}