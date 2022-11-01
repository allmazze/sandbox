node() {
    stage('Checkout') {
        git "https://github.com/allmazze/sandbox.git"
        deleteDir() // Workdir cleanup
        def scmVars = checkout scm
    }

    stage('Build') {
        sh "echo Build in progress"
        sh "apk add --update docker openrc"
        sh "service docker start"
        sh "service docker status"
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