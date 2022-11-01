node() {
    stage('Checkout') {
        git "https://github.com/allmazze/sandbox.git"
        deleteDir() // Workdir cleanup
        def scmVars = checkout scm
    }

    stage('Build') {
        sh "echo Build in progress"
        sh "docker build -t echo-server:1.0 ."
    }

}