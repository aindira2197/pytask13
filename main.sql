CREATE TABLE Graph (
    NodeID INT,
    NeighborID INT
);

INSERT INTO Graph (NodeID, NeighborID) 
VALUES 
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 9),
(7, 10),
(8, 11),
(9, 12);

CREATE TABLE DFS (
    NodeID INT,
    VisitOrder INT
);

CREATE TABLE BFS (
    NodeID INT,
    VisitOrder INT
);

DECLARE @StartNode INT = 1;
DECLARE @VisitOrder INT = 1;
DECLARE @CurrentNode INT = @StartNode;
DECLARE @Visited TABLE (NodeID INT);

INSERT INTO @Visited (NodeID) 
VALUES (@StartNode);

WHILE EXISTS (
    SELECT 1 
    FROM Graph 
    WHERE NodeID IN (SELECT NodeID FROM @Visited) 
    AND NeighborID NOT IN (SELECT NodeID FROM @Visited)
)
BEGIN
    INSERT INTO DFS (NodeID, VisitOrder) 
    SELECT @CurrentNode, @VisitOrder;

    SET @VisitOrder += 1;

    SET @CurrentNode = (
        SELECT TOP 1 NeighborID 
        FROM Graph 
        WHERE NodeID = @CurrentNode 
        AND NeighborID NOT IN (SELECT NodeID FROM @Visited)
    );

    INSERT INTO @Visited (NodeID) 
    VALUES (@CurrentNode);
END

DECLARE @Queue TABLE (NodeID INT);
DECLARE @VisitOrderBFS INT = 1;

INSERT INTO @Queue (NodeID) 
VALUES (@StartNode);

WHILE EXISTS (SELECT 1 FROM @Queue)
BEGIN
    DECLARE @CurrentNodeBFS INT = (SELECT TOP 1 NodeID FROM @Queue);

    INSERT INTO BFS (NodeID, VisitOrder) 
    VALUES (@CurrentNodeBFS, @VisitOrderBFS);

    SET @VisitOrderBFS += 1;

    DELETE FROM @Queue 
    WHERE NodeID = @CurrentNodeBFS;

    INSERT INTO @Queue (NodeID) 
    SELECT NeighborID 
    FROM Graph 
    WHERE NodeID = @CurrentNodeBFS 
    AND NeighborID NOT IN (SELECT NodeID FROM @Visited);

    INSERT INTO @Visited (NodeID) 
    SELECT NeighborID 
    FROM Graph 
    WHERE NodeID = @CurrentNodeBFS 
    AND NeighborID NOT IN (SELECT NodeID FROM @Visited);
END

SELECT * FROM DFS;
SELECT * FROM BFS;