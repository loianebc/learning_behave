Feature: Register product
  I as a product owner 
  Want to register and consult products
  So I can have all my stock on the store system

@test
  Scenario: Register a product
     Given I have the product information 
     #I could use setup table, parameter or scenario outline here but for the first...
     And I have access to the store system
     When I register the product
     Then the product will be register on the store system

@test
  Scenario: Consult all the products
     Given I have access to the store system
     When I consult all the product
     Then all the products will be presented