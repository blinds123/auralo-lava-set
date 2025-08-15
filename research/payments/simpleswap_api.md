# SimpleSwap API Documentation

## Overview
SimpleSwap API V3 - Public API for cryptocurrency exchanges

## Key Details
- **Rate Limit**: 50 requests per 10 seconds
- **Blocking**: IP blocked for 1 minute if rate limit exceeded
- **Contact**: partnerships@simpleswap.io for increased limits

## API Endpoints

### Available Endpoints:
1. **Currencies** - Get available cryptocurrencies
2. **Pairs** - Get available trading pairs  
3. **Estimates** - Get exchange rate estimates
4. **Ranges** - Get minimum/maximum exchange amounts
5. **Exchanges** - Create and manage exchanges
6. **Market** - Market data and information

## Integration Notes
- RESTful API design
- JSON responses
- Swagger/OpenAPI 3.0 documentation
- Supports various cryptocurrencies including BTC, ETH, XRP, LTC, EOS, XLM
- No KYC required for basic exchanges
- Supports both fixed and floating rates

## Business Model
- Cryptocurrency exchange service
- Supports crypto-to-crypto swaps
- Mobile app available (iOS/Android)
- Affiliate program available
- API integration for developers

## Payment Flow
1. Get available currencies
2. Check exchange pairs
3. Get rate estimate
4. Create exchange
5. Send funds to provided address
6. Receive exchanged cryptocurrency

## Security Features
- No registration required for basic swaps
- Non-custodial approach
- SSL/HTTPS encryption
- Rate limiting for API protection