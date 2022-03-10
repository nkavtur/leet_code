class Solution:
    def maxProfit(self, prices):
        min_price, best_diff = float("+infinity"), 0

        for current_price in prices:
            if current_price < min_price:
                max_price = min_price = current_price
            elif current_price > max_price:
                max_price = current_price

            best_diff = max(best_diff, max_price - min_price)

        return best_diff


Solution().maxProfit([7, 1, 5, 3, 6, 4])

