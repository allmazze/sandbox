node() {
    stage('Checkout') {
        git "https://github.com/allmazze/sandbox.git"
        deleteDir() // Workdir cleanup
        def scmVars = checkout scm
    }

    stage('Build') {
        sh "echo Build in progress"
        sh "docker build -t echo-server:1.0 ."
        sh "echo Build complete"
    }

    stage('Test') {
        sh "echo Tests in progress"
        sh "docker run echo-server:1.0"
        sh "curl http://localhost:3000"
        sh "echo Tests complete"
    }

    stage('Push artifact') {
        sh "echo Push in progress"
        sh "echo Push complete"
    }

}