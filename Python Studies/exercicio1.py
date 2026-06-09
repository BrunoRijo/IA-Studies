log_list = ["2026-06-08 08:15:23 INFO User login successful - userId=1045", 
    "2026-06-08 08:16:10 INFO Product added to cart - userId=1045 productId=987", 
    "2026-06-08 08:16:45 WARN Payment gateway response delayed - transactionId=TX12345", 
    "2026-06-08 08:17:02 INFO Order created - orderId=5001 userId=1045", 
    "2026-06-08 08:17:15 ERROR Payment failed - orderId=5001 reason=INSUFFICIENT_FUNDS", 
    "2026-06-08 08:18:04 INFO User logout - userId=1045",
    "2026-06-08 08:20:55 INFO User login successful - userId=2098", 
    "2026-06-08 08:21:12 INFO Product added to cart - userId=2098 productId=512", 
    "2026-06-08 08:21:30 INFO Product added to cart - userId=2098 productId=871", 
    "2026-06-08 08:22:05 INFO Order created - orderId=5002 userId=2098", 
    "2026-06-08 08:22:11 INFO Payment approved - orderId=5002 transactionId=TX12346", 
    "2026-06-08 08:23:44 WARN High memory usage detected - usage=87%", 
    "2026-06-08 08:25:01 ERROR Database connection timeout",
    "2026-06-08 08:25:12 INFO Database connection restored", 
    "2026-06-08 08:27:30 INFO User registration completed - userId=3102", 
    "2026-06-08 08:28:15 INFO Password reset requested - userId=2098", 
    "2026-06-08 08:29:44 ERROR Invalid password attempt - userId=2098", 
    "2026-06-08 08:31:02 INFO Password changed successfully - userId=2098", 
    "2026-06-08 08:32:10 WARN API rate limit reached - clientId=APP001", 
    "2026-06-08 08:34:08 INFO Scheduled backup started",
    "2026-06-08 08:36:52 INFO Scheduled backup completed", 
    "2026-06-08 08:40:16 ERROR Email service unavailable", 
    "2026-06-08 08:41:09 INFO Email service restored", 
    "2026-06-08 08:43:55 INFO User login successful - userId=1780", 
    "2026-06-08 08:44:03 INFO Product added to cart - userId=1780 productId=624", 
    "2026-06-08 08:44:50 INFO Order created - orderId=5003 userId=1780", 
    "2026-06-08 08:45:02 INFO Payment approved - orderId=5003 transactionId=TX12347", 
    "2026-06-08 08:46:33 WARN Disk usage above threshold - usage=91%", 
    "2026-06-08 08:47:20 ERROR File upload failed - fileId=IMG9382", 
    "2026-06-08 08:48:05 INFO File upload successful - fileId=IMG9383", 
    "2026-06-08 08:50:14 INFO User logout - userId=1780", 
]

# Exercício: Criar um dicionário para contar frequências de mensagens em uma lista simulada de logas

word = input("digite a palavra que voce quer pesquisar a frequencia nos logs:")

dictionary = {}
count = 0
for log in log_list: 
  log_verify_list = log.split()
  for log_verify in log_verify_list:
    if log_verify == word:
      count = count + 1

dictionary[word] = count
print(dictionary)