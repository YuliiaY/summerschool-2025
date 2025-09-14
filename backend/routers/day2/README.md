# Summerschool 2025 - Tag 2: Reasoning-Techniken

## 🎯 Lernziele

1.  **Self-Consistency**: Die Zuverlässigkeit von Modellantworten durch mehrfaches "Nachfragen" und einen Mehrheitsentscheid verbessern.
2.  **Tool Use**: Einem LLM beibringen, externe Werkzeuge (hier: einen Taschenrechner) per Function Calling zu nutzen, um seine eigenen Fähigkeiten zu erweitern.
3.  **Plan-and-Solve**: Komplexe Anfragen in kleinere, lösbare Schritte zerlegen zu lassen, bevor die endgültige Antwort generiert wird.

---

## 🚀 Deine Aufgaben

### Core Task 1: Self-Consistency bei Rechenaufgaben (ca. 30 min)

Teste, ob ein LLM bei einfachen Rechen- oder Logikaufgaben zuverlässiger wird, wenn man es mehrfach antworten lässt und die häufigste Antwort auswählt.

**Anforderungen:**
-   **Eingabe**: Eine Frage, die logisches Denken oder Kopfrechnen erfordert (z.B. "Wenn ein Zug um 14:00 Uhr startet und 2,5 Stunden braucht, wann kommt er an?").
-   **Logik**:
    1.  Stelle dieselbe Frage 5 Mal an das LLM (mit einer Temperatur > 0.5, um Varianz zu erzeugen).
    2.  Sammle die 5 Antworten.
    3.  Ermittle die häufigste Antwort (Mehrheitsvotum).
    4.  Gib die Mehrheits-Antwort als finales Ergebnis zurück.
-   **Implementierung**:
    -   Implementiere die Logik im `echo` Endpoint in `backend/routers/day2.py`.
    -   Vergleiche für 2-3 Beispielfragen das Ergebnis eines einzelnen Aufrufs mit dem Ergebnis der Self-Consistency-Methode.

### Core Task 2: Tool Use - Der Taschenrechner (ca. 30 min)

Implementiere einen einfachen Taschenrechner als externes "Tool", das das LLM bei Bedarf nutzen kann.

**Anforderungen:**
-   **Tool-Definition**: Definiere eine Funktion (z.B. `calculate(expression: str)`), die mathematische Ausdrücke auswerten kann.
-   **Function Calling**:
    -   Erstelle ein "Function Calling"-Schema, das dem LLM die `calculate`-Funktion beschreibt (Parameter, Zweck).
    -   Formuliere einen Prompt, der das LLM anweist, bei mathematischen Berechnungen in einer Anfrage zuerst die Funktion aufzurufen. Beispiel-Prompt: "Was sind 3 Äpfel plus 5 Orangen, und was kostet das bei 2€ pro Frucht?"
    -   Das LLM soll den Tool-Call `calculate("8 * 2")` generieren.
-   **Implementierung**:
    -   Integriere die Function-Calling-Logik in den `echo` Endpoint. Die Antwort an den User soll das Ergebnis der Berechnung enthalten.

### Core Task 3: Plan-and-Solve (ca. 15 min)

Lasse das LLM bei mehrstufigen Anfragen zuerst einen Plan erstellen und diesen dann abarbeiten.

**Anforderungen:**
-   **Eingabe**: Eine Aufgabe, die mehrere Schritte erfordert (z.B. "Wandle 5 Meilen in Meter um und runde auf die zweite Nachkommastelle").
-   **Logik**:
    1.  **Planungs-Schritt**: Sende einen ersten Prompt an das LLM, der es anweist, nur einen Plan in Stichpunkten zu erstellen.
        -   *Ergebnis*: `["1. Umrechnungsfaktor Meilen->km holen", "2. km->m umrechnen", "3. Ergebnis runden"]`
    2.  **Ausführungs-Schritt**: Kombiniere den ursprünglichen Prompt mit dem generierten Plan und bitte das LLM, die finale Antwort zu generieren.
-   **Implementierung**:
    -   Implementiere diesen zweistufigen Prozess. Logge sowohl den Plan als auch die finale Antwort, um den Prozess nachzuvollziehen.

---

### ⭐ Stretch Goals (für die Schnellen)

-   **Step-Back-Prompting**: Implementiere eine Variante, bei der das LLM vor der finalen Antwort eine allgemeine "Step-Back"-Frage generieren und beantworten muss (z.B. "Was ist das übergeordnete Prinzip hinter der Einheitenumrechnung?"). Vergleiche die Antwortqualität.
-   **Metriken**: Miss und vergleiche für alle Core Tasks die Latenz (Zeit) und die Token-Kosten. Erstelle eine kleine Tabelle.

---

##  deliverables

-   Füge deine Ergebnisse (Code-Snippets, Vergleichstabellen, geloggte Pläne) in diese `README.md` ein.
-   Sei bereit, deine Erkenntnisse am Ende des Labs zu teilen: Wo hat welche Technik am besten funktioniert?
