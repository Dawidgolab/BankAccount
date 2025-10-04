# 🏦 Simple Bank Application (Python)

Prosty program konsolowy w Pythonie, który symuluje działanie konta bankowego.
Użytkownik może sprawdzić stan konta, wpłacać i wypłacać pieniądze.

## 📌 Funkcjonalności

💰 Sprawdzenie stanu konta

➕ Wpłata środków

➖ Wypłata środków (z obsługą błędu, jeśli nie ma wystarczającej ilości pieniędzy)

🚪 Zakończenie programu

## 🛠️ Struktura projektu

result.py – klasy pomocnicze do obsługi wyników operacji (Result, Ok, Error)

bankfeatures.py – logika konta bankowego (stan konta, wpłaty, wypłaty)

bank.py – główny plik aplikacji z menu konsolowym

📂 Przykładowe użycie
<i>
Enter your initial balance: 1000<br>
--------------------------------------------------------------<br>
Select the option: 1.Show account | 2.Deposit | 3.Withdraw | 4.Exit: <br>
1<br>
-> Current account status: 1000 zł<br>
<br>
Select the option: 1.Show account | 2.Deposit | 3.Withdraw | 4.Exit:<br>
2<br>
How much do you want to deposit: 200<br>
-> Current account status: 1200 zł<br>
<br>
Select the option: 1.Show account | 2.Deposit | 3.Withdraw | 4.Exit:<br>
3<br>
How much do you want to withdraw: 1500<br>
You don't have enough money to do this operation<br>
-> Current account status: 1200 zł<br>
<br>
Select the option: 1.Show account | 2.Deposit | 3.Withdraw | 4.Exit:<br>
4<br>
Good Bye!!<br></i>
