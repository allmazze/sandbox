pipeline {
    agent {
        docker { image 'node:3.16-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}