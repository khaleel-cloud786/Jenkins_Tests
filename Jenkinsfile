pipeline {
  agent none
  stages {
    stage('Connect Git') {
      steps {
        git(url: 'https://github.com/khaleel-cloud786/Jenkins_Tests', branch: 'master')
        sh 'sh bashexample.sh'
      }
    }

  }
}