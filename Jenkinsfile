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
                    url: 'ssh://git@git.namecheap.net/~vadymbezditnyi/vadymbezditnyi_hw.git'
                    sh 'pwd'
                    sh 'ls -a'
            }
        }
    }
}
