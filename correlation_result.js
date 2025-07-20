// JSONP version of correlation result data
// Can be loaded as a script tag to avoid CORS issues

window.correlationResult = {
  "pair": "Avg_Basket-Net_Sales",
  "correlation": 0.665691
};

// Optional callback function support for JSONP
if (typeof correlationCallback === 'function') {
  correlationCallback(window.correlationResult);
} 