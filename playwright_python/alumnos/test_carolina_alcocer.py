const { test, expect } = require('@playwright/test');

// Test valida título
test('valida el título exacto de MDN', async ({ page }) => {
  await page.goto('https://developer.mozilla.org/en-US/docs/Web/JavaScript');
  await page.waitForTimeout(3000);
  await expect(page).toHaveTitle('JavaScript | MDN');
});

// Test valida título con regex
test('valida el título con regex (contiene "JavaScript")', async ({ page }) => {
  await page.goto('https://developer.mozilla.org/en-US/docs/Web/JavaScript');
  await expect(page).toHaveTitle(/JavaScript/);
});

// Test valida título con otra palabra clave
test('valida el título con regex (contiene "MDN")', async ({ page }) => {
  await page.goto('https://developer.mozilla.org/en-US/docs/Web/JavaScript');
  await expect(page).toHaveTitle(/MDN/);
});
