- general debugging process

  - set breakpoints
  - step through
  - process tracing
  - pause/resume process
  - evaluate expressions 
  - concurrency graphs
  - data flow tracking



- Testing

      - coverage testing: determine ratio of code tested by existing tests
      - design principles: testing for duplicated code, code complexity
      - linting/standards testing
      - beta/user testing: users test the website manually
      - a/b testing: users test multiple versions of a website
      - automated website testing (selenium)
      - pentesting: automated attacks on a website
      - client testing (browser stack, cross browser testing, virtual machines)
      - regression testing: test functionality after a change
      - black box (functional) testing: test function requirements with input/output (type of black box testing)
      - white box (structure) testing: test structure of code rather than functionality
      - code testing
        - static code testing (white box): analyze code for vulnerabilities
          - data flow tracing (PumaScan, Fortify, Checkmarx): trace data through application (as is done in code with breakpoints) to identify risk/trust mismatches
        - dynamic testing: test running application in an environment
      - unit testing: test units of code
      - integration testing: test interacting units of code or system components like layers
        - app use cases/workflows
        - API/service testing
      - hypothesis testing
      - deployment testing
      - system/structural problem type (code smell) detection: sonarqube, pmd, findbugs
