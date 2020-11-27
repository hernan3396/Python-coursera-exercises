text = "X-DSPAM-Confidence:    0.8475"

puntos_position = text.find(":")
with_whitespace = text[puntos_position+1:]

without_whitespace = with_whitespace.strip()
final_number = float(without_whitespace)

print(final_number)
