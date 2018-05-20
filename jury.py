class JuryTest:

    def jury(a, verbose=True):
        nneg = 0
        J = [a] # matrix J is used only to formatting purposes
        while len(a) > 1:
            a_ = a[::-1]
            J.append(a_)

            alpha = a_[0]/a[0]
            a = a[:-1] - alpha * a_[:-1]
            J.append(a)

            if a[0] < 0:
                nneg += 1
