pipeline {
  agent none
  stages {
    stage('Connect Git') {
      steps {
        git(url: 'https://github.com/khaleel-cloud786/Jenkins_Tests.git', branch: 'master', poll: true, credentialsId: 'khaleel-cloud786')
      }
    }

  }
}