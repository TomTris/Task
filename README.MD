run source myenv/bin/activate to active virtual enviroment

python3 + name file to run the file.
name of dataset is by default

Wie habe ich die logistische Regression implementiert und warum funktioniert sie noch, obwohl die logistische Regression speziell für binäre Klassifikationen (0:1) ist?
Tatsächlich habe ich für jede Qualitätsstufe ein Modell trainiert. Für jede Stichprobe wähle ich das Modell aus, das die höchste Wahrscheinlichkeit aufweist.

Wie bin ich bei diesem Projekt vorgegangen?
Sie können die Datei "Vorgehen_x_Verbesserung.png" öffnen. Ich hatte Schwierigkeiten und wusste nicht, wie ich diese Aufgabe angehen sollte. Ich habe einige Leute gefragt, und sie sagten alle: "Das ist eher ungewöhnlich, weil es keine typische Aufgabe eines Datenanalysten ist." Ich habe auch die logistische Regression getestet und nicht verstanden, warum das Ergebnis nur 60,6% betrug (weil es beim DSLR 99% waren).

Also musste ich nachdenken, und ich kam auf folgende Vorgehensweise: Zuerst visualisierte ich die Daten mit Histogrammen und Streudiagrammen, um zu sehen, ob es Korrelationen zwischen einem Kriterium und der Qualität gibt. Und dann vielleicht zwei Kriterien mit der Qualität? (Mit Hilfe eines Streudiagramms, aber es schien nicht vielversprechend).

Anschließend wurde mir klar, dass die Weinqualität nicht nur von den physikalisch-chemischen Eigenschaften abhängt. Deswegen visualisiere ich mal Durchschnitt- Verteilungstendenz. Und bezueglich dem Regression habe ich Logistic Regression verwendet, um herauszufinden, ob diese Eigenschaften die Qualität stark oder nur gering beeinflussen. Aber da das Ergebnis 60,5% betrug, obwohl die Qualität von 3 bis 8 reicht, ist das immer noch ziemlich hoch.

Wenn ich mehr Zeit hätte und weiter an dieser Aufgabe arbeiten würde, würde ich versuchen, die lineare Regression besser zu verstehen, einige andere Werte daraus zu interpretieren und genauer zu analysieren.

Vielen Dank fürs Lesen!
