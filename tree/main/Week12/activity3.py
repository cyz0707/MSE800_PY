from flask import Flask, request, render_template_string, redirect, url_for
app = Flask(__name__)

# A single-file template for the converter form and result
TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Temperature Converter</title>
    <style>
      body { font-family: Arial, Helvetica, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }
      h1 { color: #333; }
      form { margin-top: 20px; }
      label { display:block; margin-top:10px; }
      input, select { padding:8px; width: 100%; max-width: 320px; }
      .result { margin-top: 20px; padding: 12px; background:#f3f3f3; border-radius:6px; }
      .error { color: #900; }
    </style>
  </head>
  <body>
    <h1>Temperature Converter</h1>
    <form method="post" action="{{ url_for('convert') }}">
      <label for="value">Value</label>
      <input id="value" name="value" type="text" value="{{ value|default('') }}" required />

      <label for="from_unit">From</label>
      <select id="from_unit" name="from_unit">
        <option value="C" {% if from_unit=='C' %}selected{% endif %}>Celsius (C)</option>
        <option value="F" {% if from_unit=='F' %}selected{% endif %}>Fahrenheit (F)</option>
        <option value="K" {% if from_unit=='K' %}selected{% endif %}>Kelvin (K)</option>
      </select>

      <label for="to_unit">To</label>
      <select id="to_unit" name="to_unit">
        <option value="C" {% if to_unit=='C' %}selected{% endif %}>Celsius (C)</option>
        <option value="F" {% if to_unit=='F' %}selected{% endif %}>Fahrenheit (F)</option>
        <option value="K" {% if to_unit=='K' %}selected{% endif %}>Kelvin (K)</option>
      </select>

      <div style="margin-top:12px">
        <button type="submit">Convert</button>
      </div>
    </form>

    {% if error %}
      <div class="result error">Error: {{ error }}</div>
    {% endif %}

    {% if result is not none %}
      <div class="result">
        <strong>{{ value }}</strong> {{ from_unit }} = <strong>{{ result }}</strong> {{ to_unit }}
      </div>
    {% endif %}

    <hr style="margin-top:30px" />
    <small>Conversion formulas supported: C &lt;-&gt; F, C &lt;-&gt; K, F &lt;-&gt; K</small>
  </body>
</html>
"""


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius (C), Fahrenheit (F) and Kelvin (K)."""

    f = from_unit.upper()
    t = to_unit.upper()

    if f == t:
        return value

    if f == 'C':
        c = value
    elif f == 'F':
        c = (value - 32) * 5.0 / 9.0
    elif f == 'K':
        c = value - 273.15
    else:
        raise ValueError('Unknown from unit')

    if t == 'C':
        return c
    elif t == 'F':
        return (c * 9.0 / 5.0) + 32
    elif t == 'K':
        return c + 273.15
    else:
        raise ValueError('Unknown to unit')


@app.route('/', methods=['GET'])
def index():
    return render_template_string(TEMPLATE, value='', from_unit='C', to_unit='F', result=None, error=None)


@app.route('/convert', methods=['POST'])
def convert():
    value_raw = request.form.get('value', '').strip()
    from_unit = request.form.get('from_unit', 'C')
    to_unit = request.form.get('to_unit', 'F')

    try:
        value = float(value_raw)
    except ValueError:
        return render_template_string(TEMPLATE, value=value_raw, from_unit=from_unit, to_unit=to_unit, result=None,
                                      error='Please enter a numeric value.')

    try:
        result_val = convert_temperature(value, from_unit, to_unit)
        # format result to reasonable precision
        if abs(result_val) < 1e-6:
            result_str = '0'
        else:
            result_str = f"{result_val:.4f}".rstrip('0').rstrip('.')

        return render_template_string(TEMPLATE, value=value_raw, from_unit=from_unit, to_unit=to_unit, result=result_str,
                                      error=None)
    except Exception as e:
        return render_template_string(TEMPLATE, value=value_raw, from_unit=from_unit, to_unit=to_unit, result=None,
                                      error=str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')