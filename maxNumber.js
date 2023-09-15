/**
 * @param {number[]} prices
 * @return {number}
 */
function maxProfit(prices) {
    let globalProfit = 0;
    // minBuyPrice is set to Infinity because we can guarantee the first element will be set to the buy price 
    let minBuyPrice = Infinity;
  
    for (let i = 0; i < prices.length; i++) {
      if (minBuyPrice > prices[i]) {
        minBuyPrice = prices[i];
      }
  
      const currentProfit = prices[i] - minBuyPrice;
  
      if (currentProfit > globalProfit) {
        globalProfit = currentProfit;
      }
    }
  
    return globalProfit;  
}

const prices = [0,1,5,4,3,2,1]
const result = maxProfit(prices)
console.log('Max profit: ', result)
