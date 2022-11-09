pipeline {
    agent any

    stages {
        stage('Cleanup') {
            steps {
                deleteDir()
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/allmazze/sandbox.git'
                    sh 'pwd'
                    sh 'ls -a'
            }
        }
    }
}
