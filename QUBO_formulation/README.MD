# Parameter Optimization Flow

## Preparation

- Currency exchange rate dataset with arbitrage opportunity solutions

## Optimization Flow

1. Define objective function
   1. Separate training dataset into two parts, problems with no transactions as solutions and problems with nontrivial solutions. Ratio of these two types should be the same as our intended use case.
   2. Randomly choose x problems from the dataset. Each problem gives (calculated profitability - optimal profitability) points of score to the objective function.
   3. x can be larger if we have more computational power at hand. 100 may be a good start.
2. Define parameter bounds (guess what is reasonable)
   1. $5 < M_1, M_2 < 20$
   2. $50 < t < 200$ (SB)
   3. $0.001 < dt < 1$ (SB)
   4. $0 < c_0 < 1$ (SB)
   5. linear $a(t)$ from 0 to 1 (include in advanced optimization) (SB)
   6. $0.001 < y(t=0) < 0.1$ (probably not that important) (SB)
   7. $4 \leq M \leq 64$ (SQA)
   8. $0 < T < 500$ (SQA)
   9. $\Gamma(t)$ : piecewise linear or parametric ($At^b$ or $Ae^{bt}$) (SQA)
3. Use Nelder-Mead or Powell method to conduct bounded optimization on the objective function
   1. Nelder-Mead: https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method
   2. Powell: https://en.wikipedia.org/wiki/Powell%27s_method
   3. An implementation is available in scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
4. Use validation dataset to validate the performance of the new parameters. Compare with previous results.
   1. If any parameter is optimized to near the bounds, consider going back to step 2. and loosen up the bounds.
   2. If the validation results are very similar multiple (e.g., 10) times in a row, terminate the optimization process
