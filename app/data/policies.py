"""Dummy policy / FAQ data for all 77 BANKING77 intents."""

POLICIES: dict[str, dict] = {
    "_default": {
        "policy_text": "For general inquiries, our support team is available 24/7 to assist you.",
        "guidelines": [
            "Acknowledge the customer's concern.",
            "Provide general guidance and direct to appropriate resources.",
            "Offer to escalate if the issue is not resolved.",
        ],
    },
    "activate_my_card": {
        "policy_text": "Cards can be activated via the mobile app under 'Card Settings', by calling the activation hotline, or through online banking.",
        "guidelines": [
            "Guide customer: App → Cards → Activate Card.",
            "If app unavailable, provide the activation hotline number.",
            "Confirm card details before completing activation.",
        ],
    },
    "age_limit": {
        "policy_text": "Account holders must be at least 18 years old. Customers aged 16–17 may open a youth account with verified parental consent.",
        "guidelines": [
            "Confirm the customer's age and eligibility.",
            "Explain youth account options for under-18 applicants.",
            "Request parental consent documentation if applicable.",
        ],
    },
    "apple_pay_or_google_pay": {
        "policy_text": "Our cards are compatible with Apple Pay and Google Pay. Customers add their card via the respective wallet app on a supported device.",
        "guidelines": [
            "Confirm device compatibility (iOS for Apple Pay, Android for Google Pay).",
            "Guide through: Wallet app → Add Card → Follow on-screen prompts.",
            "Ensure the card is active and in good standing before setup.",
        ],
    },
    "atm_support": {
        "policy_text": "Cards work at any ATM displaying the Visa or Mastercard logo. Foreign ATM fees vary by account plan.",
        "guidelines": [
            "Confirm whether the customer's plan includes free ATM withdrawals.",
            "Provide information on partner ATMs with no surcharge.",
            "Advise customer to review the fee schedule for their account tier.",
        ],
    },
    "automatic_top_up": {
        "policy_text": "Automatic top-up maintains a minimum balance by debiting a linked bank account or card when the balance falls below the set threshold.",
        "guidelines": [
            "Guide customer: App → Top Up → Automatic Top Up → Enable.",
            "Confirm the linked funding source is active and has sufficient funds.",
            "Set the minimum balance threshold and top-up amount as desired.",
        ],
    },
    "balance_not_updated_after_bank_transfer": {
        "policy_text": "Bank transfers typically reflect within 1–3 business days. Instant payments may show immediately depending on the sending bank.",
        "guidelines": [
            "Verify the transfer was sent to the correct account details.",
            "Ask the customer to provide the transfer reference number.",
            "If more than 3 business days have passed, initiate a trace request.",
        ],
    },
    "balance_not_updated_after_cheque_or_cash_deposit": {
        "policy_text": "Cheque deposits have a clearing period of 3–5 business days. Cash deposits at partner locations reflect within 24 hours.",
        "guidelines": [
            "Confirm the deposit method and location.",
            "Ask for the deposit receipt or reference number.",
            "Explain the standard clearing timeline for cheques.",
        ],
    },
    "beneficiary_not_allowed": {
        "policy_text": "Transfers to certain beneficiaries may be blocked for compliance or fraud prevention. Customers may appeal through the app or support team.",
        "guidelines": [
            "Ask customer for the beneficiary's details (name, account number).",
            "Check if the beneficiary is flagged in the system.",
            "Initiate a compliance review if the block appears unwarranted.",
        ],
    },
    "cancel_transfer": {
        "policy_text": "Transfers can be cancelled if they have not yet been processed. Instant transfers cannot be recalled once sent.",
        "guidelines": [
            "Check transfer status in the system immediately.",
            "If status is 'pending', initiate cancellation.",
            "If already processed, guide customer through the refund request process.",
        ],
    },
    "card_about_to_expire": {
        "policy_text": "Replacement cards are automatically issued 30 days before expiry. Customers receive a notification when the new card is dispatched.",
        "guidelines": [
            "Confirm the card expiry date.",
            "Check whether a replacement has already been ordered.",
            "If not, manually trigger a replacement card order.",
        ],
    },
    "card_acceptance": {
        "policy_text": "Our cards are accepted wherever Visa or Mastercard is displayed, including online, in-store, and internationally.",
        "guidelines": [
            "Confirm the card network (Visa or Mastercard).",
            "Check if the merchant's region or category is supported.",
            "Advise customer to contact the merchant if card is unexpectedly declined.",
        ],
    },
    "card_arrival": {
        "policy_text": "Standard card delivery takes 5–7 business days. Express delivery (2–3 days) is available for an additional fee.",
        "guidelines": [
            "Confirm the delivery address on file.",
            "Provide the estimated delivery date.",
            "Offer to upgrade to express delivery if needed.",
        ],
    },
    "card_delivery_estimate": {
        "policy_text": "Standard delivery: 5–7 business days. Express delivery: 2–3 business days. Delivery times may vary by region.",
        "guidelines": [
            "Confirm the shipping option selected at time of order.",
            "Provide tracking number if available.",
            "Advise expected delivery date based on dispatch date.",
        ],
    },
    "card_linking": {
        "policy_text": "Cards can be linked via the app under 'Card Management'. Only cards registered in the customer's name can be linked.",
        "guidelines": [
            "Confirm card ownership matches the account name.",
            "Guide customer: App → Cards → Link a Card.",
            "Verify card details and complete the linking process.",
        ],
    },
    "card_not_working": {
        "policy_text": "A non-functioning card may be blocked, expired, or have an incorrect PIN. A replacement can be issued if the card is physically faulty.",
        "guidelines": [
            "Verify the card's status (active, blocked, or expired).",
            "Ask if the PIN was entered incorrectly multiple times.",
            "If the card is faulty, initiate a replacement card request.",
        ],
    },
    "card_payment_fee_charged": {
        "policy_text": "Some merchants apply a surcharge for card payments. The bank does not charge transaction fees, but third-party merchants may.",
        "guidelines": [
            "Confirm the fee originated from the merchant, not the bank.",
            "If incorrectly applied by the bank, initiate a refund.",
            "Advise customer to check merchant terms regarding payment surcharges.",
        ],
    },
    "card_payment_not_recognised": {
        "policy_text": "Unrecognized card payments must be reported within 60 days. The bank will investigate and may issue a provisional credit during the review.",
        "guidelines": [
            "Collect transaction details: date, amount, and merchant name.",
            "Verify whether the charge matches any pending authorizations.",
            "Initiate a dispute and inform customer of the investigation timeline.",
        ],
    },
    "card_payment_wrong_exchange_rate": {
        "policy_text": "Exchange rates for card payments are set by the card network (Visa/Mastercard) at settlement time. Disputes can be raised within 60 days.",
        "guidelines": [
            "Confirm the transaction date and currency used.",
            "Compare the applied rate against the official network rate on that date.",
            "If a significant discrepancy exists, initiate an exchange rate dispute.",
        ],
    },
    "card_swallowed": {
        "policy_text": "If a card is retained by an ATM, the customer should contact the ATM operator and the bank immediately. A replacement will be issued.",
        "guidelines": [
            "Instruct customer to note the ATM location and operator contact.",
            "Block the retained card immediately.",
            "Order a replacement card and advise on delivery timeline.",
        ],
    },
    "cash_withdrawal_charge": {
        "policy_text": "Cash withdrawal fees depend on the account plan. Some plans include free ATM withdrawals; others charge a flat fee or percentage.",
        "guidelines": [
            "Confirm the customer's account plan and associated ATM fee policy.",
            "If the fee was unexpected, verify whether it came from the bank or ATM operator.",
            "Provide a breakdown of applicable withdrawal fees.",
        ],
    },
    "cash_withdrawal_not_recognised": {
        "policy_text": "Unrecognized cash withdrawals must be reported immediately. The card will be blocked and a replacement issued while investigation proceeds.",
        "guidelines": [
            "Block the card immediately.",
            "Collect withdrawal details: ATM location, date, and amount.",
            "Initiate a dispute and file a fraud report.",
        ],
    },
    "change_pin": {
        "policy_text": "PINs can be changed via the mobile app under 'Card Settings' or at any ATM that supports PIN change services.",
        "guidelines": [
            "Guide customer: App → Cards → Change PIN.",
            "If using ATM: insert card → PIN Services → Change PIN.",
            "Confirm the new PIN is memorized and not shared.",
        ],
    },
    "compromised_card": {
        "policy_text": "A suspected compromised card must be blocked immediately. A replacement will be issued and any fraudulent transactions investigated.",
        "guidelines": [
            "Block the card immediately without delay.",
            "Review recent transactions for unauthorized activity.",
            "File a fraud report and initiate chargebacks for unauthorized charges.",
            "Order a replacement card and advise on security best practices.",
        ],
    },
    "contactless_not_working": {
        "policy_text": "Contactless payments may be disabled if the PIN limit is exceeded or the feature is turned off. It can be re-enabled in the app.",
        "guidelines": [
            "Check if contactless was disabled in app card settings.",
            "Verify the contactless limit has not been reached (requires PIN entry to reset).",
            "Guide customer: App → Cards → Card Controls → Enable Contactless.",
        ],
    },
    "country_support": {
        "policy_text": "Our card is accepted in over 150 countries. Certain regions may have restrictions due to compliance regulations.",
        "guidelines": [
            "Confirm the country the customer will be using the card in.",
            "Check if the destination is on the restricted country list.",
            "Advise customer to enable international payments before traveling.",
        ],
    },
    "declined_card_payment": {
        "policy_text": "Card payments may be declined due to insufficient funds, security locks, or merchant category restrictions.",
        "guidelines": [
            "Verify the customer has sufficient available balance.",
            "Check for any active restrictions on the card or account.",
            "Confirm the merchant category is not blocked by the customer's settings.",
        ],
    },
    "declined_cash_withdrawal": {
        "policy_text": "Cash withdrawals may be declined if the daily limit is reached, the card is restricted, or the ATM has a connectivity issue.",
        "guidelines": [
            "Check the customer's daily withdrawal limit and usage.",
            "Verify the card is not restricted for ATM use.",
            "Advise customer to try a different ATM if network issues are suspected.",
        ],
    },
    "declined_transfer": {
        "policy_text": "Transfers may be declined for reasons including insufficient balance, compliance holds, or flagged recipient details.",
        "guidelines": [
            "Confirm the customer's available balance.",
            "Check for any compliance or fraud holds on the account.",
            "Verify recipient details are correct and not restricted.",
        ],
    },
    "direct_debit_payment_not_recognised": {
        "policy_text": "Unrecognized direct debit payments can be disputed within 8 weeks under the direct debit guarantee. An immediate refund may be available.",
        "guidelines": [
            "Identify the originator of the direct debit mandate.",
            "Check if the customer authorized this mandate.",
            "Initiate a direct debit indemnity claim if the debit was unauthorized.",
        ],
    },
    "disposable_card_limits": {
        "policy_text": "Disposable virtual cards have customizable spending limits set by the customer. Default limits apply per card generation based on account plan.",
        "guidelines": [
            "Confirm current disposable card spending limits.",
            "Guide customer: App → Cards → Virtual Card → Set Limit.",
            "Explain maximum allowable limits per account plan.",
        ],
    },
    "edit_personal_details": {
        "policy_text": "Address and phone number can be updated in the app. Legal name changes require supporting identity documentation.",
        "guidelines": [
            "Guide customer: App → Profile → Personal Details → Edit.",
            "For name changes, request legal documents (deed poll, marriage certificate).",
            "Confirm changes are saved and send a confirmation notification.",
        ],
    },
    "exchange_charge": {
        "policy_text": "Currency exchange via the app uses the interbank rate with no markup during market hours. A small fee may apply on weekends.",
        "guidelines": [
            "Confirm whether the exchange occurred during or outside market hours.",
            "Explain the weekend fee policy (typically 0.5–1% markup).",
            "Advise customer to exchange on weekdays to avoid additional charges.",
        ],
    },
    "exchange_rate": {
        "policy_text": "Exchange rates are sourced from the interbank market and updated in real time during business hours (Monday–Friday).",
        "guidelines": [
            "Provide the current exchange rate for the requested currency pair.",
            "Advise that rates fluctuate and the displayed rate applies at the time of transaction.",
            "Explain any applicable fee or markup.",
        ],
    },
    "exchange_via_app": {
        "policy_text": "Currency exchange is available in the app under 'Exchange'. Funds convert instantly between the customer's currency accounts.",
        "guidelines": [
            "Guide customer: App → Exchange → Select currencies → Enter amount → Confirm.",
            "Confirm both currency accounts exist for the customer.",
            "Show the applicable rate before confirming the exchange.",
        ],
    },
    "extra_charge_on_statement": {
        "policy_text": "Unexpected statement charges should be reported within 60 days. The bank will investigate and refund erroneous charges.",
        "guidelines": [
            "Ask for the charge date, amount, and description.",
            "Check if the charge matches a subscription or recurring payment.",
            "Initiate a dispute if the charge cannot be identified.",
        ],
    },
    "failed_transfer": {
        "policy_text": "Failed transfers are returned to the sender's account within 3–5 business days. A notification is sent when the refund is processed.",
        "guidelines": [
            "Confirm transfer status and the reason for failure.",
            "Verify recipient account details for any errors.",
            "If funds are not returned within 5 business days, initiate a trace.",
        ],
    },
    "fiat_currency_support": {
        "policy_text": "We support over 30 fiat currencies including USD, EUR, GBP, JPY, AUD, CAD, and SGD. Currency accounts can be opened in the app.",
        "guidelines": [
            "Confirm which currency the customer is inquiring about.",
            "Check if the currency is on the supported list.",
            "Guide customer: App → Accounts → Add Currency Account.",
        ],
    },
    "get_disposable_virtual_card": {
        "policy_text": "Disposable virtual cards are single-use cards generated in the app. The card number changes after each use, protecting against fraud.",
        "guidelines": [
            "Guide customer: App → Cards → Get Virtual Card → Disposable.",
            "Set a spending limit and expiry if desired.",
            "Explain that the card number changes after each transaction.",
        ],
    },
    "get_physical_card": {
        "policy_text": "Physical cards can be ordered through the app. Standard delivery takes 5–7 business days; express delivery is available.",
        "guidelines": [
            "Confirm the customer's delivery address.",
            "Guide customer: App → Cards → Order Physical Card.",
            "Provide a delivery estimate and tracking number once dispatched.",
        ],
    },
    "getting_spare_card": {
        "policy_text": "A spare card can be ordered as a backup under the same account. It shares the same account limits and must be activated before use.",
        "guidelines": [
            "Confirm the customer's eligibility for a spare card.",
            "Process the spare card order and confirm the delivery address.",
            "Advise that the spare card requires activation before first use.",
        ],
    },
    "getting_virtual_card": {
        "policy_text": "Virtual cards are available instantly via the app. They can be used for online purchases and linked to digital wallets.",
        "guidelines": [
            "Guide customer: App → Cards → Get Virtual Card.",
            "Provide the card number, expiry, and CVV displayed in-app.",
            "Advise on secure handling of virtual card details.",
        ],
    },
    "lost_or_stolen_card": {
        "policy_text": "Lost or stolen cards must be blocked immediately. A replacement card will be dispatched within 5–7 business days.",
        "guidelines": [
            "Block the card immediately via the app or by contacting support.",
            "Review recent transactions for any unauthorized activity.",
            "Order a replacement card and confirm the delivery address.",
            "Advise customer to monitor the account for suspicious activity.",
        ],
    },
    "lost_or_stolen_phone": {
        "policy_text": "If a phone linked to the account is lost or stolen, the customer should log out all sessions and temporarily freeze the card.",
        "guidelines": [
            "Guide customer to log out of all sessions from another device.",
            "Temporarily freeze the card and disable digital wallet access.",
            "Advise customer to change account password and re-enable 2FA on a new device.",
        ],
    },
    "order_physical_card": {
        "policy_text": "Physical cards can be ordered through the mobile app or by contacting support. A fee may apply for replacement cards.",
        "guidelines": [
            "Verify the customer's current card status.",
            "Process the card order and confirm the delivery address.",
            "Provide delivery timeline and any applicable fee information.",
        ],
    },
    "passcode_forgotten": {
        "policy_text": "Forgotten passcodes can be reset via the app using the registered email address or biometric verification.",
        "guidelines": [
            "Guide customer: App → Login → Forgot Passcode → Reset via Email.",
            "Alternatively, verify identity through biometrics or security questions.",
            "Ensure the new passcode meets minimum security requirements.",
        ],
    },
    "pending_card_payment": {
        "policy_text": "Pending card payments are pre-authorized amounts that have not yet settled. They typically settle within 1–3 business days.",
        "guidelines": [
            "Confirm the transaction and explain the pending authorization status.",
            "Advise that funds will be released if the merchant does not settle.",
            "If pending for more than 7 days, initiate a review with the merchant.",
        ],
    },
    "pending_cash_withdrawal": {
        "policy_text": "Pending cash withdrawals may occur due to ATM connectivity issues. They typically resolve within 24 hours.",
        "guidelines": [
            "Confirm ATM location and time of withdrawal attempt.",
            "Check if cash was actually dispensed despite the pending status.",
            "If unresolved after 24 hours, initiate an ATM dispute.",
        ],
    },
    "pending_top_up": {
        "policy_text": "Top-ups may show as pending if the funding source requires processing time. Bank transfer top-ups can take 1–3 business days.",
        "guidelines": [
            "Confirm the top-up method and expected processing time.",
            "Ask for the transfer reference if funded via bank transfer.",
            "If pending beyond the expected timeline, initiate a trace.",
        ],
    },
    "pending_transfer": {
        "policy_text": "Transfers may show as pending due to compliance checks, bank processing, or cut-off times. Most resolve within 1–3 business days.",
        "guidelines": [
            "Confirm the transfer amount and destination.",
            "Check for any compliance or fraud holds on the transfer.",
            "Advise the customer of the expected resolution time.",
        ],
    },
    "pin_blocked": {
        "policy_text": "A PIN is blocked after 3 consecutive incorrect attempts. It can be unblocked via the app or by contacting support.",
        "guidelines": [
            "Confirm the PIN has been blocked (not expired or a card hardware issue).",
            "Guide customer: App → Cards → Unblock PIN or Reset PIN.",
            "If digital unblock fails, verify identity and reset manually.",
        ],
    },
    "receiving_money": {
        "policy_text": "Customers can receive money via bank transfer, peer-to-peer payment, or direct deposit using their account details.",
        "guidelines": [
            "Provide the customer's account number, sort code, and IBAN if applicable.",
            "Confirm the expected arrival time based on transfer type.",
            "Advise the sender to include a payment reference for traceability.",
        ],
    },
    "Refund_not_showing_up": {
        "policy_text": "Refunds typically take 5–10 business days to appear. The timeline depends on the merchant's processing speed.",
        "guidelines": [
            "Confirm the refund was initiated by the merchant.",
            "Ask for the merchant's confirmation or refund reference number.",
            "If beyond 10 business days, contact the merchant and consider a chargeback.",
        ],
    },
    "request_refund": {
        "policy_text": "Refund requests can be submitted for disputed transactions. The bank investigates and processes refunds for validated claims.",
        "guidelines": [
            "Collect transaction details: date, amount, and merchant name.",
            "Ask for the reason for the refund request.",
            "Submit the dispute and advise on the review timeline (5–10 business days).",
        ],
    },
    "reverted_card_payment?": {
        "policy_text": "Reverted card payments occur when a merchant cancels an authorized transaction. Funds are returned to the customer's account.",
        "guidelines": [
            "Confirm the reversion was initiated by the merchant.",
            "Advise that funds should appear within 1–5 business days.",
            "If not received within 5 days, initiate a follow-up with the merchant.",
        ],
    },
    "supported_cards_and_currencies": {
        "policy_text": "We support Visa and Mastercard networks. Over 30 fiat currencies are supported for account holding and transactions.",
        "guidelines": [
            "Confirm the specific card type or currency the customer is inquiring about.",
            "Provide the full list of supported currencies if requested.",
            "Advise on any restrictions for specific regions or currencies.",
        ],
    },
    "terminate_account": {
        "policy_text": "Account termination requests are processed within 5 business days. All funds must be withdrawn and pending transactions settled before closure.",
        "guidelines": [
            "Confirm the customer's intent to permanently close the account.",
            "Verify there are no outstanding balances, pending transactions, or open disputes.",
            "Process the closure request and send a written confirmation.",
        ],
    },
    "top_up_by_bank_transfer_charge": {
        "policy_text": "Bank transfer top-ups are free from our side. The customer's sending bank may apply its own outgoing transfer fees.",
        "guidelines": [
            "Clarify the bank does not charge for incoming bank transfer top-ups.",
            "Advise customer to check with their sending bank for outgoing fees.",
            "Provide correct bank account details for the top-up.",
        ],
    },
    "top_up_by_card_charge": {
        "policy_text": "Debit card top-ups are free. Credit card top-ups may incur a fee of up to 1.5% charged by the card issuer, not the bank.",
        "guidelines": [
            "Confirm the card type used for top-up (debit or credit).",
            "Explain the credit card surcharge policy.",
            "Suggest using a debit card or bank transfer to avoid fees.",
        ],
    },
    "top_up_by_cash_or_cheque": {
        "policy_text": "Cash or cheque top-ups are available at partner locations. Cheques take 3–5 business days to clear.",
        "guidelines": [
            "Provide the nearest partner location for cash deposits.",
            "Explain the cheque clearing timeline.",
            "Ask customer for the deposit receipt as proof of top-up.",
        ],
    },
    "top_up_failed": {
        "policy_text": "Failed top-ups may be caused by a declined card, bank restrictions, or system errors. Funds are not deducted on failure.",
        "guidelines": [
            "Confirm the top-up method and any error message shown.",
            "Verify the funding source is active and has sufficient balance.",
            "Retry the top-up or suggest an alternative funding method.",
        ],
    },
    "top_up_limits": {
        "policy_text": "Top-up limits depend on account verification level. Unverified accounts: £1,000/month. Fully verified accounts: up to £50,000/month.",
        "guidelines": [
            "Confirm the customer's current verification status.",
            "Advise on the limits applicable to their account tier.",
            "Guide customer through identity verification to increase limits if needed.",
        ],
    },
    "top_up_reverted": {
        "policy_text": "A reverted top-up means credited funds were subsequently recalled, typically due to a funding source dispute or processing error.",
        "guidelines": [
            "Identify the reason for the reversion.",
            "Check if the reversion was triggered by the sending bank.",
            "If in error, initiate a reversion appeal with the relevant parties.",
        ],
    },
    "topping_up_by_card": {
        "policy_text": "Debit card top-ups are processed instantly. The card must be in the customer's name and registered to their account.",
        "guidelines": [
            "Guide customer: App → Top Up → By Card → Enter amount → Confirm.",
            "Confirm the card is a debit card registered to the customer.",
            "Verify the top-up amount does not exceed account limits.",
        ],
    },
    "transaction_charged_twice": {
        "policy_text": "Duplicate charges must be reported immediately. The bank will investigate and refund the duplicate within 5 business days.",
        "guidelines": [
            "Collect both transaction details: date, amount, and merchant.",
            "Verify both charges appear in the transaction history.",
            "Initiate a duplicate charge dispute and advise on the resolution timeline.",
        ],
    },
    "transfer_fee_charged": {
        "policy_text": "Domestic transfers are free. International transfers may incur fees depending on the currency and destination country.",
        "guidelines": [
            "Confirm whether the transfer was domestic or international.",
            "Explain the applicable fee schedule for the transfer type.",
            "If a fee was applied in error, initiate a refund.",
        ],
    },
    "transfer_into_account": {
        "policy_text": "Incoming transfers are credited automatically. Bank transfers arrive within 1–3 business days; instant payments are immediate.",
        "guidelines": [
            "Provide the customer's account details (account number, sort code, IBAN).",
            "Advise on the expected arrival time based on transfer type.",
            "If funds do not arrive within the expected timeframe, initiate a trace.",
        ],
    },
    "transfer_not_received_by_recipient": {
        "policy_text": "If a recipient has not received a transfer, the bank will initiate a payment trace. The process may take 3–5 business days.",
        "guidelines": [
            "Confirm the transfer was sent to the correct account details.",
            "Retrieve the payment reference number.",
            "Initiate a payment trace with the receiving bank.",
        ],
    },
    "transfer_timing": {
        "policy_text": "Domestic transfers: same day or next business day. International transfers: 1–5 business days depending on destination.",
        "guidelines": [
            "Confirm the transfer type (domestic or international).",
            "Provide the expected arrival timeline.",
            "Advise that transfers after the cut-off time process the next business day.",
        ],
    },
    "unable_to_verify_identity": {
        "policy_text": "Verification may fail if documents are unclear, expired, or do not match account details. Additional documents may be requested.",
        "guidelines": [
            "Ask what document was submitted and what error message was shown.",
            "Advise on acceptable document types and quality requirements.",
            "Provide an alternative verification method if available.",
        ],
    },
    "verify_my_identity": {
        "policy_text": "Identity verification is completed via the app using a government-issued ID and a selfie. The process typically takes 1–2 business days.",
        "guidelines": [
            "Guide customer: App → Profile → Verify Identity → Upload ID.",
            "Ensure documents are clear, valid, and not expired.",
            "Inform customer of the review timeline.",
        ],
    },
    "verify_source_of_funds": {
        "policy_text": "Source of funds verification is required for large deposits or transfers. Customers must provide documentation showing the origin of funds.",
        "guidelines": [
            "Explain why source of funds verification is required (AML/KYC regulations).",
            "Request appropriate documentation (bank statements, payslips, sale agreements).",
            "Advise on the typical review timeline (3–5 business days).",
        ],
    },
    "verify_top_up": {
        "policy_text": "Large or unusual top-ups may be subject to manual verification. Customers will be asked to confirm the funding source.",
        "guidelines": [
            "Explain the reason for top-up verification.",
            "Request proof of the funding source (bank statement, transfer confirmation).",
            "Advise on the processing timeline once documents are received.",
        ],
    },
    "virtual_card_not_working": {
        "policy_text": "Virtual cards may not work if expired, frozen, or if the merchant does not accept virtual card numbers.",
        "guidelines": [
            "Check the virtual card status in the system.",
            "Verify the card is not frozen or past its expiry date.",
            "Confirm whether the merchant supports virtual card transactions.",
        ],
    },
    "visa_or_mastercard": {
        "policy_text": "Our cards are issued on the Visa or Mastercard network. The network is displayed on the physical card and in the app.",
        "guidelines": [
            "Confirm the card network from the customer's account details.",
            "Advise on any network-specific benefits or acceptance restrictions.",
            "If the customer requires a specific network, advise on upgrade eligibility.",
        ],
    },
    "why_verify_identity": {
        "policy_text": "Identity verification is a legal requirement under Anti-Money Laundering (AML) and Know Your Customer (KYC) regulations.",
        "guidelines": [
            "Explain that verification is a regulatory requirement, not optional.",
            "Assure the customer that data is handled securely and confidentially.",
            "Guide through the verification process to minimize friction.",
        ],
    },
    "wrong_amount_of_cash_received": {
        "policy_text": "If a customer receives the wrong cash amount from an ATM, they should report it immediately. The ATM will be audited.",
        "guidelines": [
            "Ask for the ATM location, date, and the requested vs. received amount.",
            "Initiate an ATM cash dispensing dispute.",
            "Advise customer the resolution may take 5–10 business days.",
        ],
    },
    "wrong_exchange_rate_for_cash_withdrawal": {
        "policy_text": "Exchange rates for ATM withdrawals are set at transaction time. Dynamic Currency Conversion (DCC) may apply if offered by the ATM operator.",
        "guidelines": [
            "Confirm if the ATM offered Dynamic Currency Conversion (DCC).",
            "Advise customer to always choose local currency to avoid DCC markup.",
            "If the rate was significantly wrong, initiate an exchange rate dispute.",
        ],
    },
}
