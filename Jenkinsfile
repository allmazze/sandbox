pipeline {
    agent any
    stages {
        stage('Docker check') {
            steps {
                sh 'echo $USER'
                sh 'pwd'
                sh 'docker version'
                deleteDir()
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/allmazze/sandbox.git'
                    sh 'pwd'
            }
        }
    }
}
