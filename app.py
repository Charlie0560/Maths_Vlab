from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    def ToReducedRowEchelonForm( M):
        if not M:
            return render_template("index.html",error="please enter matrix")
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        for r in range(rowCount):
            if lead >= columnCount:
                return
            i = r
            while M[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return
            M[i],M[r] = M[r],M[i]
            lv = M[r][lead]
            M[r] = [ mrx / float(lv) for mrx in M[r]]
            for i in range(rowCount):
                if i != r:
                    lv = M[i][lead]
                    M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
            lead += 1

    a1=request.form.get("a1")
    a2=request.form.get("a2")
    a3=request.form.get("a3")
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    b3=request.form.get("b3")
    c1=request.form.get("c1")
    c2=request.form.get("c2")
    c3=request.form.get("c3")
    mtx = [
           [float(a1),float(a2),float(a3)],
            [float(b1),float(b2),float(b3)],
            [float(c1),float(c2),float(c3)]
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)

