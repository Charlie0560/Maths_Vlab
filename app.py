from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit1():
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
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    mtx = [
           [float(a1),float(a2)],
            [float(b1),float(b2)]
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)

@app.route("/submit2", methods=["POST"])
def submit2():
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

@app.route("/submit3", methods=["POST"])
def submit3():
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
    a4=request.form.get("a4")
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    b3=request.form.get("b3")
    b4=request.form.get("b4")
    c1=request.form.get("c1")
    c2=request.form.get("c2")
    c3=request.form.get("c3")
    c4=request.form.get("c4")
    d1=request.form.get("c1")
    d2=request.form.get("c2")
    d3=request.form.get("c3")
    d4=request.form.get("c4")
    mtx = [
           [float(a1),float(a2),float(a3),float(a4)],
            [float(b1),float(b2),float(b3),float(b4)],
            [float(c1),float(c2),float(c3),float(c4)],
            [float(d1),float(d2),float(d3),float(d4)]
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)
@app.route("/submit4", methods=["POST"])
def submit4():
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
    mtx = [
           [float(a1),float(a2),float(a3)],
            [float(b1),float(b2),float(b3)],

        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)
@app.route("/submit5", methods=["POST"])
def submit5():
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
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    c1=request.form.get("c1")
    c2=request.form.get("c2")
    mtx = [
           [float(a1),float(a2)],
            [float(b1),float(b2)],
            [float(c1),float(c2)],
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)
@app.route("/submit6", methods=["POST"])
def submit6():
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
    a4=request.form.get("a4")
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    b3=request.form.get("b3")
    b4=request.form.get("b4")
    c1=request.form.get("c1")
    c2=request.form.get("c2")
    c3=request.form.get("c3")
    c4=request.form.get("c4")
    mtx = [
           [float(a1),float(a2),float(a3),float(a4)],
            [float(b1),float(b2),float(b3),float(b4)],
            [float(c1),float(c2),float(c3),float(c4)],
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)



@app.route("/submit7", methods=["POST"])
def submit7():
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
    a4=request.form.get("a4")
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    b3=request.form.get("b3")
    b4=request.form.get("b4")
    mtx = [
           [float(a1),float(a2),float(a3),float(a4)],
            [float(b1),float(b2),float(b3),float(b4)],
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)
@app.route("/submit8", methods=["POST"])
def submit8():
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
    b1=request.form.get("b1")
    b2=request.form.get("b2")
    c1=request.form.get("c1")
    c2=request.form.get("c2")
    d1=request.form.get("d1")
    d2=request.form.get("d2")
    mtx = [
           [float(a1),float(a2)],
            [float(b1),float(b2)],
            [float(c1),float(c2)],
            [float(d1),float(d2)]
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)



@app.route("/submit9", methods=["POST"])
def submit9():
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
    d1=request.form.get("d1")
    d2=request.form.get("d2")
    d3=request.form.get("d3")
    mtx = [
           [float(a1),float(a2),float(a3)],
            [float(b1),float(b2),float(b3)],
            [float(c1),float(c2),float(c3)],
            [float(d1),float(d2),float(d3)]
        ]


    ToReducedRowEchelonForm( mtx )
    return render_template("index.html",rowform=mtx)
