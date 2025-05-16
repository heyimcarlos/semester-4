using Microsoft.VisualStudio.TestTools.UnitTesting;
using MyMath;

namespace MyMath.Tests;

[TestClass]
public sealed class Test1
{
    [TestMethod]
    public void BasicRooterTest()
    {
        Rooter rooter = new Rooter();

        double expected = 2.0;
        double input = expected * expected;
        double actual = rooter.SquareRoot(input);


        Assert.AreEqual(expected, actual, expected / 100);
    }

    [TestMethod]
    public void RooterValueRange()
    {
        Rooter rooter = new Rooter();

        for (double expected = 1e-8; expected < 1e+8; expected = expected * 3.2)
        {
            RooterOneValue(rooter, expected);
        }
    }

    private void RooterOneValue(Rooter rooter, double expected)
    {
        double input = expected * expected;
        double actual = rooter.SquareRoot(input);
        Assert.AreEqual(expected, actual, delta: expected / 100);
    }
}
