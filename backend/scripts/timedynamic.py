import numpy as np
from numpy.core.numerictypes import ScalarType
from numpy.lib.function_base import append
from numpy.linalg import eig
from scipy.linalg import solve
import json

DEBUG = True

# Values are for default struct with [0, 1, 0, 0] incoming coefficients
vv11 = np.array([complex(0.0, -0.121293), complex(-0.61281, 0.0), complex(0.0, 0.121293), complex(0.61281, 0.0)], dtype=complex) # np.array([complex(-0.121293, 5.97957*(10**-18)), complex(0.121293, 2.89059*(10**-17)), complex(5.33339*(10**-16), -0.61281), complex(4.43682*(10**-17), 0.61281)], dtype=complex)
vv12 = np.array([complex(0.0, 0.600474), complex(0.0442088, 0.0), complex(0.0, -0.600474), complex(-0.0442088, 0.0)], dtype=complex) # np.array([complex(0.600474, 1.65551*(10**-17)), complex(-0.600474, 4.76095*(10**-16)), complex(-1.83054*(10**-16), 0.0442088), complex(-1.92455*(10**-16), -0.0442088)], dtype=complex)
vv13 = np.array([complex(0.0, -0.788343), complex(0.0, -0.156218), complex(0.0, -0.788343), complex(0.0, -0.156218)], dtype=complex) # np.array([complex(0.788343, 0), complex(0.788343, 0), complex(-0.156218, -1.0639*(10**-16)), complex(-0.156218, -3.73559*(10**-17))], dtype=complex)
vv14 = np.array([complex(0.0, 0.0568719), complex(0.0, 0.773373), complex(0.0, 0.0568719), complex(0.0, 0.773373)], dtype=complex) # np.array([complex(-0.0568719, -1.6194*(10**-16)), complex(-0.0568719, 2.85786*(10**-16)), complex(0.773373, 0), complex(0.773373, 0)], dtype=complex)

vv21 = np.array([complex(0.0, 0.482924), complex(0.0831366, 0.0), complex(0.0, -0.482924), complex(-0.0831366, 0.0)], dtype=complex) # np.array([complex(-0.482924, -3.30323*(10**-18)), complex(0.482924, 1.67514*(10**-17)), complex(-0.0831366, -2.8195*(10**-17)), complex(-0.0831366, 7.03906*(10**-17))], dtype=complex)
vv22 = np.array([complex(0.0, -0.128803), complex(-0.872776, 0.0), complex(0.0, 0.128803), complex(0.872776, 0.0)], dtype=complex) # np.array([complex(0.128803, 6.98095*(10**-17)), complex(-0.128803, 9.25412*(10**-17)), complex(0.872776, 0), complex(0.872776, 0)], dtype=complex)
vv23 = np.array([complex(0.0, -0.0821325), complex(0.0, 0.464742), complex(0.0, -0.0821325), complex(0.0, 0.464742)], dtype=complex) # np.array([complex(-0.0821325, 9.36681*(10**-18)), complex(-0.0821325, -1.29001*(10**-17)), complex(-1.29383*(10**-16), 0.464742), complex(-8.46814*(10**-18), -0.464742)], dtype=complex)
vv24 = np.array([complex(0.0, 0.862234), complex(0.0, -0.123954), complex(0.0, 0.862234), complex(0.0, -0.123954)], dtype=complex) # np.array([complex(0.862234, 0), complex(0.862234, 0), complex(-3.97554*(10**-18), -0.123954), complex(-9.25688*(10**-17), 0.123954)], dtype=complex)

mathematica_vectors = np.array([[vv11, vv12, vv13, vv14],
                                [vv21, vv22, vv23, vv24],
                                [vv11, vv12, vv13, vv14]], dtype=complex)

ee1 = np.array([complex(0.0, 1.90425), complex(-0.360895, 0.0), complex(0.0, -1.90425), complex(0.360895, 0.0)], dtype=complex) # np.array([complex(2.09202*(10**-16), -1.90425), complex(4.44089*(10**-16), 1.90425), complex(0.360895, -9.86973*(10**-18)), complex(-0.360895, -8.73395*(10**-17))], dtype=complex)
ee2 = np.array([complex(0.0, 1.67391), complex(-0.107923, 0.0), complex(0.0, -1.67391), complex(0.107923, 0.0)], dtype=complex) # np.array([complex(-3.33067*(10**-16), -1.67391), complex(-2.22045*(10**-16), 1.67391), complex(0.107923, -1.6017*(10**-17)), complex(-0.107923, -8.92287*(10**-18))], dtype=complex)

mEE = [ee1, ee2, ee1]

def calcFactors(pyV, pyVals):
    print('Factors:')
    ratios = []
    print('pyV: (',len(pyV) , ',', pyV[0].shape, ')')
    print('mVV: ( 3 , (4, 4) )')
    for i in range(2):
        print('layer ', i+1)
        print('values')
        print(pyVals[i])
        print(mEE[i])
        for j in range(4):
            print('vector ', j)
            py = np.transpose(pyV[i][j])
            m = mathematica_vectors[i][j]
            print(py)
            print(m)
            print('\n')
            ratio = np.divide(py, m)
            ratios.append(ratio)
        print('Ratios: ')
        if (i == 0):
            for ratio in ratios[0:4]:
                print(ratio)
                print('\n')
        else:
            for ratio in ratios[4:8]:
                print(ratio)
                print('\n')
    return ratios

def range_at_1(end):
    return range(1, end+1)

def expDiagonal(eigVals, zNorm):
    tmp = [eigVals[0], eigVals[1], eigVals[2], eigVals[3]]
    return np.diag(np.exp(np.multiply(tmp,zNorm)))

def swapArrayIndices(a, i, j):
    if (DEBUG):
        print('Swapping ' + str(a[i]) + ' and ' + str(a[j]))
    a[i], a[j] = a[j], a[i]
    return a

def swapMatrixRows(a, i, j):
    if (DEBUG):
        print('row swap ' + str(i) + ' and ' + str(j))
    a[[i,j],:] = a[[j,i],:]
    return a

def swapMatrixColumns(a, i, j):
    # print('Matrix Before Swap: ', a)
    if (DEBUG):
        print('row swap ' + str(i) + ' and ' + str(j))
    a[:,[i,j]] = a[:,[j,i]]
    # print('Matrix After Swap: ', a)
    return a

def isNumZero(num):
    precision = 1e-6
    return (num < precision and num > -precision) or num == 0

def organizeEigen(val, vec):
    for i in range(4):
        # print('vec ', i, vec)
        v = val[i]
        imaginary = (not isNumZero(v.imag)) and (isNumZero(v.real))
        real = (isNumZero(v.imag)) and (not isNumZero(v.real))
        if imaginary:
            if (DEBUG):
                print('Eigenvalue ' + str(v) + ' is imaginary')
            if (v.imag < 0) and (not i == 0):
                if (DEBUG):
                    print('Eigenvalue ' + str(v) + ' is negative imaginary. Swapping to front!')
                val = swapArrayIndices(val, i, 0)
                vec = swapMatrixColumns(vec, i, 0)
            elif not i == 2:
                if (DEBUG):
                    print('Eigenvalue ' + str(v) + ' is positive imaginary. Swapping to 3rd slot!')
                val = swapArrayIndices(val, i, 2)
                vec = swapMatrixColumns(vec, i, 2)
        elif real:
            if (DEBUG):
                print('Eigenvalue ' + str(v) + ' is real')
            if (v.real > 0) and (not i == 1):
                if (DEBUG):
                    print('Eigenvalue ' + str(v) + ' is positive real. Swapping to second entry!')
                val = swapArrayIndices(val, i, 1)
                vec = swapMatrixColumns(vec, i, 1)
    t4 = val[3]
    if ((not isNumZero(t4.imag)) and (isNumZero(t4.real))):
        if (DEBUG):
                print('Eigenvalue ' + str(t4) + ' is imaginary')
        if (t4.imag < 0) :
            if (DEBUG):
                print('Eigenvalue ' + str(t4) + ' is negative imaginary. Swapping to third!')
            val = swapArrayIndices(val, 3, 2)
            vec = swapMatrixColumns(vec, 3, 2)
    # vec = swapMatrixColumns(vec, 3, 2)
    return val, vec

def organizeEigenForMiddleLayers(val, vec):
    for i in range(4):
        v = val[i]
        imaginary = (not isNumZero(v.imag)) and (isNumZero(v.real))
        real = (isNumZero(v.imag)) and (not isNumZero(v.real))
        if imaginary:
            if v.imag > 0 and i != 0:
                val = swapArrayIndices(val, i, 0)
                vec = swapMatrixColumns(vec, i, 0)
            if v.imag < 0 and i != 1:
                val = swapArrayIndices(val, i, 1)
                vec = swapMatrixColumns(vec, i, 1)
        elif real:
            if v.real > 0 and i != 2:
                val = swapArrayIndices(val, i, 2)
                vec = swapMatrixColumns(vec, i, 2)
            if v.real < 0 and i != 3:
                val = swapArrayIndices(val, i, 3)
                vec = swapMatrixColumns(vec, i, 3)

    return val, vec


# Classes for storing structure data
class Structure:
    # Sub class for defining each layer
    class Layer:
        # Instance variables for each Layer object
        def __init__(self, name, length, epsilon, mu, vvo, ee):
            if (DEBUG):
                print('     Instanciating Layer')
            self.name = name
            self.length = length
            self.epsilon = epsilon
            self.mu = mu
            self.solution = np.zeros(4, dtype=complex)
            self.eigVec = [np.zeros((4,1), dtype=complex)] * 4
            self.eigVal = [np.zeros(4)]
            self.vvo = vvo
            self.ee = ee

        def __str__(self):
            try:
                return self.name + ': ' + str(self.length) + '\nEigen: ' + self.eigVal + self.eigVec
            except:
                return self.name + ': ' + str(self.length)

        def getEigVal(self):
            return self.eigVal
        
        def getEps(self):
            return self.epsilon

        def getMu(self):
            return self.mu

        def getLength(self):
            return self.length

    # Instance variables for each Structure object
    def __init__(self, num, omega, k1, k2, startI):
        if (DEBUG):
            print('Instanciating Structure')
        self.num = num
        self.omega = omega
        self.c = 1
        self.kap = omega/self.c
        self.k1 = k1/self.kap
        self.k2 = k2/self.kap
        self.layers = []
        self.transferMatrices = []
        self.startingIndex = startI

    def printLayers(self):
        print('\nLAYERS: ')
        for layer in self.layers:
            print(layer)

    def removeLayer(self, n):
        if (DEBUG):
            print('Removing Layer')
        self.layers.pop(n)

    # Method for adding a layer to the structure
    def addLayer(self, name, length, epsilon, mu, vvo, ee):
        if (DEBUG):
            print('Adding Layer')
        l = self.Layer(name, length, epsilon, mu, vvo, ee)
        self.layers.append(l)

    # Method for inserting a layer into given index n
    def insertLayer(self, name, length, epsilon, mu, n, vvo, ee):
        if (DEBUG):
            print('Inserting Layer')
        l = self.Layer(name, length, epsilon, mu, vvo, ee)
        self.layers.insert(n, l)

    # Create the maxwell matrices
    # The matrix is derived from Maxwell's ODEs
    def buildMatrices(self):
        if (DEBUG):
            print('\nBuilding Maxwell')
        maxwell_matrices = []
        for layer in self.layers:
            e = layer.epsilon
            u = layer.mu
            k1 = self.k1
            k2 = self.k2
            imaginary = complex(0, 1)
            omega = self.omega * imaginary
            m11 = omega * (-(e[2][0]*k1/e[2][2]) - (k2*u[1][2]/u[2][2]))
            m12 = omega * (-(e[2][1]*k1/e[2][2]) + (k1*u[1][2]/u[2][2]))
            m13 = omega * ((k1*k2/e[2][2]) + u[1][0] -
                        (u[1][2]*u[2][0]/u[2][2]))
            m14 = omega * ((-k1 ** 2/e[2][2]) + u[1]
                        [1] - (u[1][2]*u[2][1]/u[2][2]))
            m21 = omega * (-(e[2][0]*k2/e[2][2]) - (k2*(u[0][2]/u[2][2])))
            m22 = omega * (-(e[2][1]*k2/e[2][2]) - (k1*u[0][2]/u[2][2]))
            m23 = omega * ((k2 ** 2/e[2][2]) - u[0]
                        [0] + (u[0][2]*u[2][0]/u[2][2]))
            m24 = omega * (-(k1*k2/e[2][2]) - u[0]
                        [1] + (u[0][2]*u[2][1]/u[2][2]))
            m31 = omega * (-e[1][0] + (e[1][2]*e[2][0] /
                                    e[2][2]) - (k1*k2/u[2][2]))
            m32 = omega * (-e[1][1] + (e[1][2]*e[2][1] /
                                    e[2][2]) + (k1 ** 2/u[2][2]))
            m33 = omega * (-(e[1][2]*k2/e[2][2]) - (k1*u[2][0]/u[2][2]))
            m34 = omega * ((e[1][2]*k1/e[2][2]) - (k1*u[2][1]/u[2][2]))
            m41 = omega * (e[0][0] - (e[0][2]*e[2][0] /
                                    e[2][2]) - (k2 ** 2/u[2][2]))
            m42 = omega * (e[0][1] - (e[0][2]*e[2][1] /
                                    e[2][2]) + (k1*k2/u[2][2]))
            m43 = omega * ((e[0][2]*k2/e[2][2]) - (k2*u[2][0]/u[2][2]))
            m44 = omega * (-(e[0][2]*k1/e[2][2]) - (k2*u[2][1]/u[2][2]))
            maxwell_matrix = np.matrix([[m11,  m12, m13, m14],
                                        [m21,  m22, m23, m24],
                                        [m31,  m32, m33, m34],
                                        [m41,  m42, m43, m44]], dtype=complex)
            maxwell_matrices.append(maxwell_matrix)
            if (DEBUG):
                print('Maxwells :', maxwell_matrix)
        self.maxwell = maxwell_matrices
        return maxwell_matrices

    # Import maxwell matrices into struct
    def importMatrices(self, matrices):
        if (DEBUG):
            print('\nImporting Maxwell from Data')
        self.maxwell = matrices

    def printMaxwell(self):
        print('Maxwells:')
        for m in self.maxwell:
            print(m)

    # Calculate the eigenproblem for all layers of the structure
    def calcEig(self):
        if (DEBUG):
            print('\nCalculating Eigen Problem')
        for n in range(len(self.layers)):
            if (DEBUG):
                print('For layer ' + str(n+1))
            #start = time.perf_counter()
            eigVal, eigVec = np.linalg.eig(self.maxwell[n])
            # eigVal, eigVec = eig(self.maxwell[n])[0], eig(self.maxwell[n])[1]
            # print(eigVal, eigVec)
            # for i in range(4):
            #     self.layers[n].eigVec[i] = np.transpose(eigVec[i])
            if n == 0 or n == self.num - 1:
                self.layers[n].eigVal, self.layers[n].eigVec = organizeEigen(eigVal, eigVec)
            else:
                self.layers[n].eigVal, self.layers[n].eigVec = organizeEigenForMiddleLayers(eigVal, eigVec)
            if (DEBUG):
                Av = np.multiply(self.maxwell[n], np.transpose(eigVec))
                lambdaV = np.multiply(eigVal, np.transpose(eigVec))
                print('LAYER ', n)
                print('Av: ', Av)
                print('lambda v: ', lambdaV)
                print('Av = lambda v: ', Av == lambdaV)
            #eigVal, eigVec = organizeEigen(eigVal, eigVec)
            #end = time.perf_counter()
            #print(f'Time to calculate Eigensystem: {end-start:0.5f} seconds')
            if (DEBUG):
                print(f'Values:\n{self.layers[n].eigVal}')
            if (DEBUG):
                print(f'Vectors:\n{self.layers[n].eigVec}')

    # Import preexisting eigendata
    def importEig(self, e_vals, e_vecs):
        if (DEBUG):
            print('\nImporting previously created eigendata')
        for n in range(len(self.layers)):
            print("I'M WORKING")
            if(DEBUG):
                print(f'Eigenvalue array {n}:\n{e_vals[n]}')
                print(f'Eigenvector array {n}:\n{e_vecs[n]}')
            self.layers[n].eigVal = e_vals[n]
            self.layers[n].eigVec = e_vecs[n]

    def calcModes(self):
        if (DEBUG):
            print('\nCalculating Modes')
        for layer in self.layers:
            mode = np.zeros((1,4), dtype=complex)
            for n in range(4):
                mode += np.multiply(np.multiply(np.real(layer.eigVec[n]), np.exp(np.real(layer.eigVal[n]))), layer.length)
            layer.modes = mode
            if (DEBUG):
                print(str(layer.name) + ' Modes:\nc*' + str(layer.modes))

    def interfaces(self):
        interfaces = []
        print("Interface")
        #print(-self.layers[0].getLength())
        interfaces.append(self.startingIndex)
        for i in range(self.num):
            interfaces.append(interfaces[i] + self.layers[i].getLength())
        return interfaces


    def calcScattering(self):
        # if (not DEBUG):
            # self.debugEigV()
        layers = self.num
        I = layers - 1
        s = np.zeros((4*I,4*layers), dtype=complex)
        references = np.zeros(layers)   # zref
        ifaces = self.interfaces()      # zzz
        interfaces = np.zeros(I)        # zz
        leftPsi = [np.zeros(4)] * I
        rightPsi = [np.zeros(4)] * I
        # Calculate the reference points
        for i in range(layers):
            # The first layer reference point is the right endpoint
            if i < 2:
                references[i] = 0
            # Calculate the rest of the reference points, the left endpoint
            else:
                references[i] = (ifaces[i] - ifaces[i-1])
        # Calculate the locations (z-values) of the interfaces
        for i in range(I):
            # First interface is always at 0
            if i == 0:
                interfaces[i] = 0
            # Next interface is the endpoint of the following layer
            else:
                interfaces[i] = ifaces[i+1]
        if(DEBUG):
            print(interfaces)
            print(references)
            print(ifaces)
        for i in range(I):
            expVecLeft = np.exp((self.layers[i].eigVal * (interfaces[i] - references[i])))
            expVecRight = np.exp((self.layers[i+1].eigVal * (interfaces[i] - references[i+1])))
            if(DEBUG):
                print('expVecLeft:')
                print(expVecLeft)
                print('expVecRight:')
                print(expVecRight)
            leftPsi[i] = np.dot(self.layers[i].eigVec, np.diag(expVecLeft))
            rightPsi[i] = np.dot(self.layers[i+1].eigVec, np.diag(expVecRight))
        if(DEBUG):
            print('leftPsi: ')
            print(leftPsi)
            print('rightPsi: ')
            print(rightPsi)
        for inter in range_at_1(I):
            for i in range_at_1(4):
                for j in range_at_1(4):
                    vali = (4 * (inter - 1) + i) - 1
                    valj = (4 * (inter - 1) + j) - 1
                    valj2 = 4 * inter + j - 1
                    # print('indices: ')
                    # print(vali, valj)
                    # print(vali, valj2)
                    s[vali][valj] = leftPsi[inter-1].item(i-1,j-1)
                    s[vali][valj2] = np.negative(rightPsi[inter-1].item(i-1,j-1))
        # s = s.transpose()
        # for inter in range(I):
        #     for i in range(4):
        #         for j in range(4):
        #             s[4*inter+i][4*inter+j] = leftPsi[inter].item(i,j)
        #             s[4*inter+i][4*(inter+1)+j] = -rightPsi[inter].item(i,j)
                    # s[4*(inter-1)+(i)-1][4*(inter-1)+(j)-1] = leftPsi[inter].item(i,j)
                    # s[4*(inter-1)+(i)-1][4*(inter)+(j)-1] = -rightPsi[inter].item(i,j)
        if(DEBUG):
            print('Scattering matrix')
            print(s.shape)
            print(s[0:4])
            print(s[4:8])
            # print(s)
            print("\n")
        self.scattering = s
        return s
    

    # Calculate the constants for each layer to be used in the fields/solutions
    def calcConstants(self, c1, c2, c3, c4):
        scattering = self.calcScattering()
        layers = self.num
        interfaces = layers-1
        s = np.zeros((4*interfaces,4*interfaces), dtype=complex)
        b = np.zeros(4*interfaces, dtype=complex)
        # s = scattering
        for i in range(4*interfaces):
            for j in range(4*interfaces):
                s[i][j] = scattering[i][j+2]
        if(DEBUG):
            print('Condensed Scattering matrix')
            print(s.shape)
            print(s[0:4])
            print(s[4:8])
        for i in range_at_1(4):
            # b[i-1] = np.subtract(b.item(i-1), np.subtract(np.multiply(scattering[i-1][0],c1),np.multiply(scattering[i-1][1],c2)))
            b[i-1] = b.item(i-1) - (scattering[i-1][0] * c1) - (scattering[i-1][1] * c2)
            aug1 = 4*(interfaces-1)+i-1
            aug2 = 4*(interfaces+1)-2
            aug3 = 4*(interfaces+1)-1
            b[aug1] = b.item(aug1) - (scattering[aug1][aug2] * c3) - (scattering[aug1][aug3] * c4)
            # b[aug1] = np.subtract(b.item(aug1), np.subtract(np.multiply(scattering[aug1][aug2],c3),np.multiply(scattering[aug1][aug3],c4)))
        # for i in range(4):
        #     f[i] = np.subtract(f.item(i), np.subtract(np.multiply(scattering[i][0],c1),np.multiply(scattering[i][1],c2)))
        #     aug1 = 4*(interfaces-1)+i-1
        #     aug2 = 4*(interfaces+1)-2
        #     aug3 = 4*(interfaces+1)-1
        #     f[aug1] = np.subtract(f.item(aug1), np.subtract(np.multiply(scattering[aug1][aug2],c3),np.multiply(scattering[aug1][aug3],c4)))
        #     f[4*(interfaces-1)+i] = f[4*(interfaces-1)+i] - scattering[4*(interfaces-1)+i][4*(interfaces+1)-1]*c3 - scattering[4*(interfaces-1)+i][4*(interfaces+1)-1]*c4
        # b is ff in mathematica code
        # s is ss in mathematica code
        if(DEBUG):
            print('b')
            print(b)
        cPrime = solve(s,b)
        # cPrime is bb in mathematica code
        c = np.zeros(4*layers, dtype=complex) # Constants vector
        c[0] = c1
        c[1] = c2
        c[4*layers-2] = c3
        c[4*layers-1] = c4
        for i in range(4*interfaces):
            c[i+2] = cPrime[i]
        # print(c)
        # The following is code in mathematica that is currently missing
        # c = np.zeros((layers,4), dtype=complex)
        # for layer in range_at_1(interfaces):
        #     for j in range_at_1(4):
        #         c[layer-1][j-1] = b[4*(layer-1)+j-1]
        self.constants = c
        for i in range(self.num):
            for j in range(4):
                # Set solution equal to the mode times the constant
                sol = self.layers[i].modes[0][j] * c[i*4+j]
                # Store solution in the structure layer
                self.layers[i].solution[j] = sol
        # print('scattering: ', str(s))
        # print('constants: ', str(c))
        # print('b: ', str(b))
        # cs = (np.matmul(s,cPrime))
        # print('S*c:', str(cs))
        # print(cs == b)
        return c
    
    def determineFieldAtSpecificPointInLayer(self, z, layer):
        z_ends = self.interfaces()
        interfaces = [0] * self.num
        current_c = self.constants[layer*4:4+(layer*4)]
        num_layers = self.num

        for z in range(num_layers):
            if z < num_layers - 1:
                interfaces[z] = 0
            else:
                interfaces[z] = z_ends[z] - z_ends[z-1]

        piScalar = np.pi * 0.4
        scalar = np.exp(np.multiply(complex(0.0, 1.0), piScalar))
        scalarMat = np.multiply(scalar, self.layers[layer].eigVec)
        expDiag = np.diag(np.exp(np.multiply(self.layers[layer].eigVal, (z - interfaces[layer]))))
        expMat = np.matmul(scalarMat, expDiag)
        fieldVec = np.matmul(expMat, current_c)
        return fieldVec
    
    def determineField(self, e, ee, u, uu, k1, k2, num_points=400):
            print("Determine Field:")
            self.k1 = k1
            self.k2 = k2
            self.ee = ee
            self.e = e
            ep = np.row_stack(([e], [ee], [e]))
            self.u = u 
            self.uu = uu
            mu = np.row_stack(([u], [uu], [u]))
            num_layers = self.num
            z_ends = self.interfaces()              # zzz
            interfaces = [0] * (self.num - 1)       # zz
            references = np.zeros(num_layers)       # zref
            z_arr = []
            Ex = []
            Ey = []
            Hx = []
            Hy = []
            e3 = []
            h3 = []
             

            # Calculate the reference points
            for i in range(num_layers):
                # The first layer reference point is the right endpoint
                if i == 0:
                    references[i] = 0
                # Calculate the rest of the reference points, the left endpoint
                else:
                    references[i] = z_ends[i]
            # Calculate the locations (z-values) of the interfaces
            for i in range(num_layers-1):
                # First interface is always at 0
                if i == 0:
                    interfaces[i] = 0
                # Next interface is the endpoint of the following layer
                else:
                    interfaces[i] = z_ends[i+1]

            for layer in range(num_layers):
                length = z_ends[layer+1] - z_ends[layer]

                current_c = self.constants[layer*4:4+(layer*4)]

                if (DEBUG):
                    print("Constant vector at layer " + str(layer))
                    print(current_c)

                piScalar = np.pi * 0.4
                scalar = np.exp(np.multiply(complex(0.0, 1.0), piScalar))
                scalarMat = np.multiply(scalar, self.layers[layer].vvo)
                
                for i in range(num_points):
                    z = z_ends[layer] + i*length/ num_points
                    z_arr.append(z)
                    expDiag = np.diag(np.exp(np.multiply((z - references[layer]), self.layers[layer].ee)))
                    expMat = np.dot(scalarMat, expDiag)

                    fieldVec = np.matmul(expMat, current_c)
                    f = open("output.txt", "a")
                    print(z, file = f)
                    print(fieldVec, file = f)
                    #field0 = np.transpose(fieldVec)

            #print(z_arr)

                    # e1 = field0[0:3]
                    # e2 = field0[1::3]

                    # e3mock = np.array(-((ep[layer, 2, 0] * e1 + (ep[layer,2,1] * e2 - k2 * h1 + k1 * h2 / (ep[layer, 2, 2])))))
                    # h3mock = np.array(- (k2 * e1 - k1 * e2 + (mu[layer, 2, 0] * h1) + (mu[layer, 2, 1] * h2 / (mu[layer, 2, 2]))))
                    
            

                    z_arr.append(z)
                    Ex.append(fieldVec.item(0).real)
                    Ey.append(fieldVec.item(1).real)
                    Hx.append(fieldVec.item(2).real)
                    Hy.append(fieldVec.item(3).real)
                    # e3.append(e3mock.real)
                    # h3.append(h3mock.real)


                    field = {
                        'z': z_arr,
                        'Ex': Ex,
                        'Ey': Ey,
                        'Hx': Hx,
                        'Hy': Hy,
                        #'e3': e3, 
                        #'h3': h3
                    }





    # Calculate the modes. Result will not contain constant multiplication
    # def calcFields(self, e, ee, u, uu, k1, k2, npoints=400):
    #     if (DEBUG):
    # #         print('\nCalculating Fields')
    #     self.ee = ee
    #     self.e = e
    #     ep = np.row_stack(([e], [ee], [e]))
    #     self.u = u 
    #     self.uu = uu
    #     mu = np.row_stack(([u], [uu], [u]))
    #     z_ends = self.interfaces()   
    #     num_layers = self.num
    #     for layer in range(num_layers):
    #         self.k1 = k1
    #         self.k2 = k2
    #         current_c = self.constants[layer*4:4+(layer*4)]
    #         references = np.zeros(num_layers)  
    #         if layer < 2:
    #             references[layer] = 0
    #         # Calculate the rest of the reference points, the left endpoint
    #         else:
    #             references[layer] = (z_ends[layer] - z_ends[layer-1])
    #         for i in range(npoints):
    #             length = z_ends[layer+1] - z_ends[layer]
    #             z = z_ends[layer] + i * length / npoints
    #             print("zzzzz", z)
    #                 piScalar = np.pi * 0.4
    #                 scalar = np.exp(np.multiply(complex(0.0, 1.0), piScalar))
    #                 scalarMat = np.multiply(scalar, self.layers[layer].eigVec)
    #                 expDiag = np.diag(np.exp(np.multiply(self.layers[layer].eigVal, (z - references[layer]))))
    #                 expMat = np.matmul(scalarMat, expDiag)
    #                 fieldVec = np.matmul(expMat, current_c)
    #                 field0 = np.transpose(fieldVec)[:4]
    #                 e3 = -(((ep[layer, 2, 0] * field0[[0]])+ (ep[layer,2,1] * field0[[1]]) - k2 * field0[[2]] + k1 * field0[[3]]) / (ep[layer, 2, 2]))
    #                 h3 = - ((k2 * field0[[0]] - k1 * field0 [[1]] + (mu[layer, 2, 0] * field0[[2]]) + (mu[layer, 2, 1] * field0[[3]])) / (mu[layer, 2, 2]))
    #                 print('first e', z, e3[[0]])
    #                 print('first h', z, h3[[0]])
         


def test():
    print('Starting Test:')
    size = 3
    omega = 0.398
    k1 = 0.5
    k2 = 0.22
    s = Structure(size, omega, k1, k2, -15)
    e = np.array([[1.5,0,0],
                [0,8,0],
                [0,0,1]])
    ee = np.array([[8,0,0],
                [0,1.5,0],
                [0,0,1]])
    u = np.array([[4,0,0],
                [0,1,0],
                [0,0,1]])
    uu = np.array([[1,0,0],
                [0,4,0],
                [0,0,1]])

    vvo1 = np.array([vv11, vv12, vv13, vv14])
    vvo2 = np.array([vv21, vv22, vv23, vv24])
    vvo3 = np.array([vv11, vv12, vv13, vv14])
    s.addLayer('Ambient Left', 15, e, u, vvo1, ee1)
    s.addLayer('Layer 1', 7, e, u, vvo2, ee2)
    s.addLayer('Layer 2', 15, e, u, vvo3, ee1)
    #s.addLayer('Ambient Right', 7, e, u)
    s.printLayers()
    s.removeLayer(1)
    s.printLayers()
    s.insertLayer('Layer 1', 7, ee, uu, 1, vvo2, ee2)
    s.printLayers()
    m = s.buildMatrices()
    print('Number of Layers: ' + str(len(m)))
    print('Dimension of 1st layer Maxwell: ' + str(m[0].shape))
    print('Dimension of 2nd layer Maxwell: ' + str(m[1].shape))
    print('Dimension of 3rd layer Maxwell: ' + str(m[2].shape))
    print(s)
    s.printMaxwell()
    s.calcEig()
    s.calcModes()
    c1 = 0
    c2 = 1
    c3 = 0
    c4 = 0
    s.calcConstants(c1,c2,c3,c4)
    s.determineField(e, ee, u, uu, k1, k2)
#    s.calcFields(e, ee, u, uu, k1, k2)
#    s.fields(e, ee, u, uu)

def main():
    print("Starting Test!")
    test()
    print("Finished Test!")

main()
