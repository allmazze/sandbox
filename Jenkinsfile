node() {
    stage('Checkout') {
        git "https://github.com/allmazze/sandbox.git"
        deleteDir() // Workdir cleanup
        def scmVars = checkout scm
    }

    stage('Build') {
        sh "echo Build in progress"
        sh "sudo apt-get update"
        sh "sudo apt-get -y install apt-transport-https ca-certificates curl"
        sh "curl -fsSL https://get.docker.com -o get-docker.sh"
        sh "sudo sh get-docker.sh"
        sh "echo Build complete"
    }

    stage('Test') {
        sh "echo Tests in progress"
        sh "echo Tests complete"
    }

    stage('Push artifact') {
        sh "echo Push in progress"
        sh "echo Push complete"
    }

}