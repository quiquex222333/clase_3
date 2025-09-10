// cypress_js/alumnos/pablo_delgadillo.cy.js

describe('Google Search con Cypress', () => {
  it('debe tener el título correcto', () => {
    cy.visit('https://google.com/')
    cy.title().should('include', 'Google')
  })

  function searchText(text) {
    cy.visit('https://google.com/')
    cy.get('input[name="q"]').click().type(text)
    cy.get('input[name="btnK"]').click()
    cy.title().should('include', text)
  }
})